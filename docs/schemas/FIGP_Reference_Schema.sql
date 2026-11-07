-- FIGP v1: SQLite reference model. DESIGN ONLY. Do not run on the user's host.
PRAGMA foreign_keys = ON;
CREATE TABLE IF NOT EXISTS source_record (
  source_id TEXT PRIMARY KEY,
  publisher TEXT NOT NULL,
  source_uri TEXT NOT NULL,
  rights_status TEXT NOT NULL CHECK(rights_status IN ('unknown','metadata-only','licensed','open','prohibited')),
  sha256 TEXT,
  signature_status TEXT NOT NULL DEFAULT 'unverified',
  retrieved_at TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS framework_family (
  family_id TEXT PRIMARY KEY,
  publisher TEXT NOT NULL,
  canonical_name TEXT NOT NULL,
  kind TEXT NOT NULL,
  canonical_uri TEXT,
  metadata_json TEXT NOT NULL DEFAULT '{}',
  UNIQUE(publisher, canonical_name)
);
CREATE TABLE IF NOT EXISTS framework_release (
  release_id TEXT PRIMARY KEY,
  family_id TEXT NOT NULL REFERENCES framework_family(family_id),
  source_id TEXT REFERENCES source_record(source_id),
  release_label TEXT NOT NULL,
  publication_date TEXT,
  effective_from TEXT,
  effective_to TEXT,
  release_status TEXT NOT NULL DEFAULT 'current',
  sha256 TEXT,
  UNIQUE(family_id, release_label)
);
CREATE TABLE IF NOT EXISTS framework_part (
  part_id TEXT PRIMARY KEY,
  release_id TEXT NOT NULL REFERENCES framework_release(release_id),
  parent_part_id TEXT REFERENCES framework_part(part_id),
  part_label TEXT NOT NULL,
  part_type TEXT NOT NULL,
  UNIQUE(release_id, part_label)
);
CREATE TABLE IF NOT EXISTS graph_node (
  node_id TEXT PRIMARY KEY,
  node_kind TEXT NOT NULL CHECK(node_kind IN ('requirement','canonical-control','threat','vulnerability','asset','evidence','legal-obligation','other')),
  release_id TEXT REFERENCES framework_release(release_id),
  external_key TEXT,
  payload_json TEXT NOT NULL DEFAULT '{}'
);
CREATE TABLE IF NOT EXISTS requirement (
  requirement_id TEXT PRIMARY KEY,
  node_id TEXT NOT NULL UNIQUE REFERENCES graph_node(node_id),
  release_id TEXT NOT NULL REFERENCES framework_release(release_id),
  part_id TEXT REFERENCES framework_part(part_id),
  native_control_id TEXT NOT NULL,
  source_anchor TEXT,
  rights_status TEXT NOT NULL DEFAULT 'metadata-only',
  UNIQUE(release_id, native_control_id)
);
CREATE TABLE IF NOT EXISTS graph_edge (
  edge_id TEXT PRIMARY KEY,
  from_node_id TEXT NOT NULL REFERENCES graph_node(node_id),
  to_node_id TEXT NOT NULL REFERENCES graph_node(node_id),
  relation TEXT NOT NULL CHECK(relation IN ('part_of','version_of','supersedes','amends','references','maps_to','partially_maps_to','supports','implements','evaluates','evidenced_by','mitigates','detects','related_to','applies_to','conflicts_with')),
  source_id TEXT REFERENCES source_record(source_id),
  confidence REAL CHECK(confidence >= 0 AND confidence <= 1),
  review_status TEXT NOT NULL DEFAULT 'proposed' CHECK(review_status IN ('proposed','reviewed','approved','rejected','stale')),
  rationale TEXT NOT NULL DEFAULT '',
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(from_node_id,to_node_id,relation,source_id)
);
CREATE TABLE IF NOT EXISTS project_snapshot (
  snapshot_id TEXT PRIMARY KEY,
  project_alias TEXT NOT NULL,
  source_fingerprint TEXT NOT NULL,
  parser_version TEXT NOT NULL,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  classification TEXT NOT NULL DEFAULT 'private'
);
CREATE TABLE IF NOT EXISTS evidence (
  evidence_id TEXT PRIMARY KEY,
  snapshot_id TEXT NOT NULL REFERENCES project_snapshot(snapshot_id),
  control_node_id TEXT NOT NULL REFERENCES graph_node(node_id),
  test_id TEXT NOT NULL,
  result TEXT NOT NULL CHECK(result IN ('pass','fail','inconclusive','not-applicable','not-tested')),
  evidence_sha256 TEXT,
  classification TEXT NOT NULL DEFAULT 'private',
  expires_at TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS applicability_rule (
  rule_id TEXT PRIMARY KEY,
  jurisdiction TEXT NOT NULL,
  sector TEXT,
  entity_type TEXT,
  condition_json TEXT NOT NULL,
  legal_basis_uri TEXT NOT NULL,
  review_status TEXT NOT NULL DEFAULT 'proposed'
);
CREATE TABLE IF NOT EXISTS proposal (
  proposal_id TEXT PRIMARY KEY,
  snapshot_id TEXT NOT NULL REFERENCES project_snapshot(snapshot_id),
  diff_ref TEXT NOT NULL,
  diff_sha256 TEXT NOT NULL,
  risk TEXT NOT NULL,
  state TEXT NOT NULL DEFAULT 'draft' CHECK(state IN ('draft','assessed','awaiting-approval','approved','staged-for-external-application','closed','rejected')),
  expires_at TEXT,
  created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS review_event (
  review_id TEXT PRIMARY KEY,
  target_kind TEXT NOT NULL,
  target_id TEXT NOT NULL,
  action TEXT NOT NULL,
  reviewer_role TEXT NOT NULL,
  actor_ref TEXT NOT NULL,
  event_time TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
  rationale TEXT NOT NULL DEFAULT ''
);
CREATE INDEX IF NOT EXISTS idx_framework_release_family ON framework_release(family_id);
CREATE INDEX IF NOT EXISTS idx_requirement_release ON requirement(release_id);
CREATE INDEX IF NOT EXISTS idx_graph_edge_from ON graph_edge(from_node_id);
CREATE INDEX IF NOT EXISTS idx_graph_edge_to ON graph_edge(to_node_id);
CREATE INDEX IF NOT EXISTS idx_graph_edge_review ON graph_edge(review_status);
CREATE INDEX IF NOT EXISTS idx_evidence_snapshot ON evidence(snapshot_id);
