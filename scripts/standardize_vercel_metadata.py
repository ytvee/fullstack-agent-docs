#!/usr/bin/env python3
import argparse
import pathlib
import re
from collections import Counter
from urllib.parse import urlparse


DASH_LINE = "-" * 80
ROOT = pathlib.Path(__file__).resolve().parents[1]
VERCEL_DIR = ROOT / "knowledge" / "official" / "devops" / "vercel"
CURRENT_DATE = "2026-04-07"

STOPWORDS = {
    "a",
    "an",
    "and",
    "api",
    "app",
    "apps",
    "at",
    "by",
    "for",
    "from",
    "how",
    "in",
    "into",
    "is",
    "its",
    "learn",
    "manage",
    "managing",
    "of",
    "on",
    "or",
    "overview",
    "reference",
    "the",
    "to",
    "using",
    "use",
    "with",
    "without",
    "your",
    "vercel",
    "docs",
}

GENERIC_TITLE_WORDS = {
    "account",
    "advanced",
    "all",
    "anatomy",
    "api",
    "app",
    "build",
    "code",
    "configuring",
    "create",
    "creating",
    "deployment",
    "deploying",
    "getting",
    "guide",
    "help",
    "image",
    "input",
    "install",
    "installation",
    "integration",
    "introduction",
    "learn",
    "limits",
    "list",
    "manage",
    "managing",
    "overview",
    "pricing",
    "quickstart",
    "reference",
    "settings",
    "started",
    "troubleshoot",
    "troubleshooting",
    "understanding",
    "usage",
    "using",
    "vercel",
    "documentation",
    "what",
    "working",
}

SPECIAL_TAG_PATTERNS = [
    (r"\bai gateway\b", "ai-gateway"),
    (r"\bai sdk\b", "ai-sdk"),
    (r"\bopenresponses\b", "openresponses"),
    (r"\bresponses api\b", "responses-api"),
    (r"\bchat completions\b", "chat-completions"),
    (r"\bstructured outputs?\b", "structured-outputs"),
    (r"\btool calls?\b|\btool calling\b", "tool-calling"),
    (r"\bembeddings\b", "embeddings"),
    (r"\bstreaming\b", "streaming"),
    (r"\bimage input\b", "image-input"),
    (r"\bactivity log\b", "activity-log"),
    (r"\baudit log", "audit-logs"),
    (r"\bpasskeys?\b", "passkeys"),
    (r"\bsaml\b|\bsingle sign-on\b", "saml-sso"),
    (r"\boidc\b|openid connect", "oidc"),
    (r"\bmcp\b|model context protocol", "mcp"),
    (r"\bweb analytics\b", "web-analytics"),
    (r"\bspeed insights\b", "speed-insights"),
    (r"\bobservability\b", "observability"),
    (r"\balerts?\b", "alerts"),
    (r"\bcron jobs?\b", "cron-jobs"),
    (r"\bedge config\b", "edge-config"),
    (r"\bedge middleware\b", "edge-middleware"),
    (r"\bedge runtime\b", "edge-runtime"),
    (r"\bfluid compute\b", "fluid-compute"),
    (r"\benvironment variables?\b", "environment-variables"),
    (r"\bcustom domains?\b", "custom-domains"),
    (r"\bpreview deployment", "preview-deployments"),
    (r"\bdeployment protection\b", "deployment-protection"),
    (r"\bdeploy hooks?\b", "deploy-hooks"),
    (r"\bdeploy button\b", "deploy-button"),
    (r"\bfeature flags?\b", "feature-flags"),
    (r"\bflags explorer\b", "flags-explorer"),
    (r"\bimage optimization\b", "image-optimization"),
    (r"\bincremental static regeneration\b|\bisr\b", "isr"),
    (r"\bmicrofrontends?\b", "microfrontends"),
    (r"\bmonorepos?\b", "monorepos"),
    (r"\bremote caching\b", "remote-caching"),
    (r"\bturborepo\b", "turborepo"),
    (r"\bnx\b", "nx"),
    (r"\bdns\b", "dns"),
    (r"\bssl\b|\bcertificates?\b", "ssl"),
    (r"\bopenai\b", "openai"),
    (r"\banthropic\b", "anthropic"),
    (r"\bxai\b", "xai"),
    (r"\bpython\b", "python"),
    (r"\bnode\.?js\b", "nodejs"),
    (r"\bruby\b", "ruby"),
    (r"\brust\b", "rust"),
    (r"\bwasm\b|webassembly", "wasm"),
    (r"\bbun\b", "bun"),
    (r"\bfastapi\b", "fastapi"),
    (r"\bexpress\b", "express"),
    (r"\bfastify\b", "fastify"),
    (r"\bflask\b", "flask"),
    (r"\bhono\b", "hono"),
    (r"\bkoa\b", "koa"),
    (r"\bnestjs\b", "nestjs"),
    (r"\bnuxt\b", "nuxt"),
    (r"\bremix\b", "remix"),
    (r"\bsveltekit\b", "sveltekit"),
    (r"\bastro\b", "astro"),
    (r"\bgatsby\b", "gatsby"),
    (r"\bvite\b", "vite"),
    (r"\breact router\b", "react-router"),
    (r"\btanstack start\b", "tanstack-start"),
    (r"\bnext\.?js\b", "nextjs"),
    (r"\bopenfeature\b", "openfeature"),
]

CATEGORY_EXACT_MAP = {
    "accounts": "accounts",
    "activity-log": "observability",
    "agent": "agent",
    "agent-resources": "integrations",
    "ai-gateway": "ai-gateway",
    "ai-sdk": "ai-gateway",
    "alerts": "observability",
    "analytics": "analytics",
    "audit-log": "observability",
    "bot-management": "security",
    "botid": "security",
    "build-output-api": "builds",
    "builds": "builds",
    "caching": "caching",
    "cdn": "caching",
    "cdn-cache": "caching",
    "cdn-security": "security",
    "checks": "checks",
    "cli": "cli",
    "code-owners": "code-owners",
    "comments": "comments",
    "conformance": "conformance",
    "connectivity": "connectivity",
    "cron-jobs": "cron-jobs",
    "custom-error-pages": "errors",
    "deploy-button": "deployments",
    "deployment-checks": "deployments",
    "deployment-protection": "deployments",
    "deployment-retention": "deployments",
    "deploy-hooks": "deployments",
    "deployments": "deployments",
    "directory-listing": "deployments",
    "directory-sync": "deployments",
    "dns": "dns",
    "domains": "domains",
    "draft-mode": "deployments",
    "drains": "observability",
    "edge-config": "edge-config",
    "edge-middleware": "functions",
    "edit-mode": "deployments",
    "environment-variables": "environment-variables",
    "errors": "errors",
    "flags": "flags",
    "fluid-compute": "functions",
    "frameworks": "frameworks",
    "functions": "functions",
    "fundamentals": "root",
    "getting-started-with-vercel": "root",
    "git": "deployments",
    "glossary": "root",
    "headers": "headers",
    "how-vercel-cdn-works": "caching",
    "image-optimization": "image-optimization",
    "incremental-migration": "deployments",
    "incremental-static-regeneration": "frameworks",
    "instant-rollback": "deployments",
    "integrations": "integrations",
    "limits": "plans",
    "logs": "observability",
    "manage-and-optimize-observability": "observability",
    "marketplace-storage": "integrations",
    "mcp": "mcp",
    "microfrontends": "microfrontends",
    "monorepos": "monorepos",
    "multi-tenant": "multi-tenant",
    "notebooks": "root",
    "notifications": "accounts",
    "observability": "observability",
    "og-image-generation": "og-image-generation",
    "oidc": "security",
    "open-source-program": "root",
    "package-managers": "root",
    "plans": "plans",
    "rbac": "accounts",
    "security": "security",
    "storage": "integrations",
}

TYPE_HINTS_GUIDE = (
    "getting started",
    "quickstart",
    "installation",
    "install ",
    "using ",
    "working with",
    "managing ",
    "how ",
    "configuring ",
    "debugging ",
    "troubleshooting",
    "troubleshoot",
    "rotating ",
    "deploying ",
    "creating ",
    "migrating ",
    "connect to ",
    "add ",
    "set up ",
    "setup",
)

TYPE_HINTS_CONCEPT = (
    "overview",
    "what is",
    "introduction",
    "pricing",
    "plan",
    "plans",
    "glossary",
    "concepts",
    "features",
    "fundamental",
    "understanding",
)


def slugify(value: str) -> str:
    value = value.lower()
    value = value.replace("&", " and ")
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value).strip("-")
    return value


def split_camel(value: str) -> str:
    return re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", value)


def parse_top_block(text: str):
    patterns = [
        re.compile(r"\A---\n(?P<body>.*?)\n---\n?", re.S),
        re.compile(r"\A" + re.escape(DASH_LINE) + r"\n(?P<body>.*?)\n" + re.escape(DASH_LINE) + r"\n?", re.S),
    ]
    for pattern in patterns:
        match = pattern.match(text)
        if not match:
            continue
        raw = match.group("body")
        meta = {}
        for line in raw.splitlines():
            m = re.match(r'^([a-zA-Z0-9_]+):\s*(.*)$', line)
            if not m:
                continue
            key = m.group(1)
            value = m.group(2).strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            meta[key] = value
        return meta, match.end()
    return {}, 0


def find_h1(text: str):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def extract_headings(text: str):
    return [m.group(1).strip() for m in re.finditer(r"^#{2,3}\s+(.+)$", text, re.M)]


def sentence_summary(text: str):
    body = re.sub(r"\A(```.*?```|---.*?---|" + re.escape(DASH_LINE) + r".*?" + re.escape(DASH_LINE) + r")", "", text, flags=re.S)
    lines = []
    for line in body.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#") or stripped.startswith(">") or stripped.startswith("```"):
            continue
        if stripped.startswith("<") and stripped.endswith(">"):
            continue
        lines.append(stripped)
        if len(" ".join(lines)) > 220:
            break
    joined = " ".join(lines)
    joined = re.sub(r"\s+", " ", joined).strip()
    if len(joined) <= 160:
        return joined
    parts = re.split(r"(?<=[.!?])\s+", joined)
    summary = ""
    for part in parts:
        if not part:
            continue
        candidate = (summary + " " + part).strip()
        if len(candidate) > 160 and summary:
            break
        summary = candidate
    return summary[:160].rstrip()


def source_segments(source: str):
    if not source:
        return []
    path = urlparse(source).path
    if not path.startswith("/docs"):
        return []
    rest = path[len("/docs"):].strip("/")
    if not rest:
        return []
    return [slugify(seg) for seg in rest.split("/") if seg]


def infer_topic_and_subcategory(fname: str, title: str, description: str, source: str):
    if fname == "vercel.md":
        return "root", "root"
    segments = source_segments(source)
    if not segments and source.endswith("/docs"):
        return "root", "root"
    top = segments[0] if segments else ""
    second = segments[1] if len(segments) > 1 else ""
    text = " ".join(x for x in [fname, title, description, source] if x).lower()

    if "managed infrastructure" in text or "miu" in text:
        return "plans", "managed-infrastructure"
    if top == "multi-tenant" and "domain" in text:
        return "domains", "multi-tenant"
    if top == "oidc" and any(x in text for x in ("aws", "azure", "gcp", "federation", "openid")):
        return "security", "oidc"
    if top == "agent-resources":
        return "integrations", "agent-resources"
    if top == "integrations":
        return "integrations", "integrations"
    if top == "activity-log":
        return "observability", "activity-log"
    if top == "audit-log":
        return "observability", "audit-log"
    if top == "alerts":
        return "observability", "alerts"
    if top == "drains":
        return "observability", "drains"
    if top == "logs":
        return "observability", "logs"
    if top == "headers":
        return "headers", "headers"
    if top == "mcp":
        return "mcp", "mcp"

    topic = CATEGORY_EXACT_MAP.get(top, top or slugify(title or pathlib.Path(fname).stem))
    subcategory = top or topic

    if not topic:
        topic = slugify(pathlib.Path(fname).stem)
    if not subcategory:
        subcategory = topic

    if topic == "root" and top and top not in {"root"}:
        subcategory = top
    if top == "contentful" and "managed infrastructure" in text:
        subcategory = "managed-infrastructure"
    return topic, subcategory


def is_integration_page(title: str, description: str, source: str, topic: str, subcategory: str):
    text = " ".join(x for x in [title, description, source] if x).lower()
    segments = source_segments(source)
    top = segments[0] if segments else ""
    specific_framework = bool(re.search(r"\bon vercel\b", title.lower()))
    framework_overview = any(
        phrase in title.lower()
        for phrase in (
            "frameworks on vercel",
            "supported frameworks",
            "frontends on vercel",
            "backends on vercel",
            "full-stack frameworks",
        )
    )
    agent_tool = top == "agent-resources" and any(seg in source for seg in ("coding-agents", "integrations-for-models"))
    if top in {"integrations"}:
        return True
    if top == "frameworks" and specific_framework and not framework_overview:
        return True
    if top == "oidc" and any(x in text for x in ("aws", "azure", "gcp")):
        return True
    if agent_tool and not any(
        phrase in title.lower()
        for phrase in ("coding agents", "framework integrations", "ecosystem", "build with ai")
    ):
        return True
    return topic == "integrations"


def infer_type(title: str, description: str, source: str, topic: str, subcategory: str, fname: str):
    if fname == "vercel.md":
        return "concept"
    title_l = title.lower()
    text = " ".join(x for x in [title, description, source, topic, subcategory] if x).lower()
    if "changelog" in title_l or "/changelog" in source:
        return "changelog"
    if "examples" in title_l or title_l.endswith(" demo") or "sample" in title_l:
        return "example"
    if "reference" in title_l or "api reference" in title_l or "/reference/" in source or "/api-reference" in source:
        return "api-reference"
    if topic == "cli" and title_l.startswith("vercel "):
        return "api-reference"
    if topic == "errors":
        return "guide"
    if is_integration_page(title, description, source, topic, subcategory):
        return "integration"
    if any(hint in title_l for hint in TYPE_HINTS_CONCEPT):
        return "concept"
    if any(hint in text for hint in TYPE_HINTS_GUIDE):
        return "guide"
    if topic in {"plans", "root", "analytics", "observability", "flags"} and any(word in text for word in ("pricing", "plan", "overview", "concept", "features", "limits")):
        return "concept"
    if topic in {"functions", "checks"} and title_l.startswith("vercel ") and any(word in title_l for word in ("api", "reference", "logs", "certs", "dns", "env", "deploy", "list", "open", "pull", "project")):
        return "api-reference"
    return "concept"


def title_tokens(title: str):
    cleaned = split_camel(title)
    words = re.findall(r"[A-Za-z0-9.+#]+", cleaned)
    tokens = []
    for word in words:
        slug = slugify(word)
        if not slug or slug in STOPWORDS or slug in GENERIC_TITLE_WORDS:
            continue
        tokens.append(slug)
    return tokens


def heading_tags(headings):
    tags = []
    for heading in headings[:12]:
        lower = heading.lower()
        if "saml" in lower or "single sign-on" in lower:
            tags.append("saml-sso")
        elif "passkey" in lower:
            tags.append("passkeys")
        elif "team membership" in lower:
            tags.append("team-membership")
        elif "default team" in lower:
            tags.append("default-team")
        elif "environment variable" in lower:
            tags.append("environment-variables")
        elif "edge config" in lower:
            tags.append("edge-config")
        elif "rate limit" in lower:
            tags.append("rate-limits")
        else:
            slug = slugify(heading)
            if 3 <= len(slug) <= 32:
                tags.append(slug)
    return tags


def infer_tags(title: str, description: str, source: str, headings, category: str, subcategory: str, doc_type: str):
    text = " ".join(x for x in [title, description, source, " ".join(headings[:12])] if x)
    tags = []
    for pattern, tag in SPECIAL_TAG_PATTERNS:
        if re.search(pattern, text, re.I):
            tags.append(tag)
    for token in title_tokens(title):
        if token not in tags:
            tags.append(token)
    for seg in source_segments(source)[1:4]:
        if seg and seg not in tags and seg not in STOPWORDS:
            tags.append(seg)
    for tag in heading_tags(headings):
        if tag not in tags:
            tags.append(tag)

    title_slug = slugify(title)
    if (
        title_slug
        and not title_slug.startswith("vercel-")
        and title_slug not in tags
        and len(title_slug.split("-")) <= 4
        and len(title_slug) <= 28
        and title_slug not in {category, subcategory}
    ):
        tags.insert(0, title_slug)

    if doc_type == "api-reference":
        for extra in ("api-reference", "cli-command", "reference"):
            if extra not in tags and extra not in {category, subcategory}:
                tags.append(extra)
                if len(tags) >= 6:
                    break
    elif doc_type == "guide":
        for extra in ("setup", "how-to", "troubleshooting"):
            if extra not in tags and extra not in {category, subcategory}:
                tags.append(extra)
                if len(tags) >= 6:
                    break
    elif doc_type == "integration":
        for extra in ("integration",):
            if extra not in tags and extra not in {category, subcategory}:
                tags.append(extra)

    cleaned = []
    excluded = {"vercel", category, subcategory, category.replace("vercel-", "")}
    for tag in tags:
        tag = slugify(tag)
        if not tag or tag in excluded or tag in STOPWORDS:
            continue
        if tag.startswith("vercel-") or len(tag) > 28:
            continue
        if tag not in cleaned:
            cleaned.append(tag)
    return cleaned[:6] if len(cleaned) >= 3 else (cleaned + [subcategory, doc_type])[:3]


def derive_error_slug(title: str):
    if re.fullmatch(r"[A-Z0-9_]+", title):
        return slugify(title)
    return ""


def make_yaml_array(items):
    return "[" + ", ".join(f'"{item}"' for item in items) + "]"


def tokenize_for_similarity(*parts):
    tokens = set()
    for part in parts:
        if not part:
            continue
        for token in title_tokens(part):
            if token and token not in STOPWORDS:
                tokens.add(token)
        for pattern, tag in SPECIAL_TAG_PATTERNS:
            if re.search(pattern, part, re.I):
                tokens.add(tag)
    return tokens


def compute_related(records):
    by_name = {record["filename"]: record for record in records}
    for record in records:
        scores = []
        for other in records:
            if other["filename"] == record["filename"]:
                continue
            if other["filename"] == "vercel.md" and record["filename"] != "vercel.md":
                continue
            score = 0
            if other["category"] == record["category"]:
                score += 35
            if other["subcategory"] == record["subcategory"]:
                score += 20
            if other["source_segments"] and record["source_segments"]:
                if other["source_segments"][0] == record["source_segments"][0]:
                    score += 8
                if len(other["source_segments"]) > 1 and len(record["source_segments"]) > 1:
                    if other["source_segments"][:2] == record["source_segments"][:2]:
                        score += 10
                shared_source_segments = len(set(other["source_segments"]) & set(record["source_segments"]))
                score += shared_source_segments * 3
                shorter = min(len(other["source_segments"]), len(record["source_segments"]))
                if shorter >= 2:
                    if other["source_segments"][:shorter] == record["source_segments"][:shorter]:
                        score += 6
            shared_tags = len(set(record["tags"]) & set(other["tags"]))
            score += shared_tags * 6
            shared_tokens = len(record["sim_tokens"] & other["sim_tokens"])
            score += shared_tokens * 4
            if record["type"] == other["type"]:
                score += 2
            if "getting-started" in other["filename"] and other["category"] == record["category"]:
                score += 4
            if "reference" in other["filename"] and other["category"] == record["category"]:
                score += 4
            if "troubleshoot" in other["filename"] and other["category"] == record["category"]:
                score += 3
            if score >= 18:
                scores.append((score, other["filename"]))
        scores.sort(key=lambda item: (-item[0], item[1]))
        record["related"] = [name for _, name in scores[:3]]
        if record["filename"] == "vercel.md":
            record["related"] = []
        if not record["related"]:
            record["related"] = []
    return by_name


def build_record(path: pathlib.Path):
    text = path.read_text(encoding="utf-8")
    meta, block_end = parse_top_block(text)
    body = text[block_end:]
    title = meta.get("title", "").strip() or find_h1(text).strip() or slugify(path.stem).replace("-", " ").title()
    description = meta.get("description", "")
    if not description:
        description = sentence_summary(text)
    source = meta.get("source", "")
    last_updated = meta.get("last_updated", "") or CURRENT_DATE
    if path.name == "vercel.md":
        title = "Vercel Documentation"
        description = "Combined Vercel documentation snapshot for the full source."
        source = "https://vercel.com/docs"
    headings = extract_headings(text)
    topic, subcategory = infer_topic_and_subcategory(path.name, title, description, source)
    category = f"vercel-{topic}"
    doc_type = infer_type(title, description, source, topic, subcategory, path.name)
    tags = infer_tags(title, description, source, headings, category, subcategory, doc_type)
    if path.name == "vercel.md":
        tags = ["documentation", "reference", "snapshot", "combined-docs"]
    error_slug = derive_error_slug(title)
    if error_slug and error_slug not in tags and len(tags) < 6:
        tags.insert(0, error_slug)
    tags = tags[:6]
    if len(tags) < 3:
        fallback = [slugify(path.stem.split("-", 1)[-1]), subcategory, doc_type]
        for tag in fallback:
            if tag and tag not in tags and tag not in {subcategory, category.replace("vercel-", "")}:
                tags.append(tag)
            if len(tags) >= 3:
                break

    document_key_match = re.match(r"^(\d{4})-", path.name)
    if path.name == "vercel.md":
        doc_id = "vercel-root"
    elif document_key_match:
        doc_id = f'vercel-{document_key_match.group(1)}'
    else:
        doc_id = f'vercel-{slugify(path.stem)}'

    sim_tokens = tokenize_for_similarity(title, description, source, " ".join(headings[:8]), " ".join(tags))
    return {
        "path": path,
        "filename": path.name,
        "body": body,
        "title": title,
        "description": description,
        "source": source,
        "last_updated": last_updated,
        "category": category,
        "subcategory": subcategory,
        "type": doc_type,
        "tags": tags[:6],
        "id": doc_id,
        "sim_tokens": sim_tokens,
        "source_segments": source_segments(source),
    }


def render_frontmatter(record):
    return (
        "---\n"
        f'id: "{record["id"]}"\n'
        f'title: "{record["title"].replace(chr(34), chr(92) + chr(34))}"\n'
        f'description: "{record["description"].replace(chr(34), chr(92) + chr(34))}"\n'
        f'category: "{record["category"]}"\n'
        f'subcategory: "{record["subcategory"]}"\n'
        f'type: "{record["type"]}"\n'
        f'source: "{record["source"].replace(chr(34), chr(92) + chr(34))}"\n'
        f'tags: {make_yaml_array(record["tags"])}\n'
        f'related: {make_yaml_array(record["related"])}\n'
        f'last_updated: "{record["last_updated"]}"\n'
        "---\n"
    )


def rewrite_record(record, dry_run=False):
    path = record["path"]
    text = path.read_text(encoding="utf-8")
    _, block_end = parse_top_block(text)
    body = text[block_end:]
    new_text = render_frontmatter(record) + body
    if not dry_run:
        path.write_text(new_text, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include-0001", action="store_true")
    args = parser.parse_args()

    paths = sorted(VERCEL_DIR.glob("*.md"))
    records = [build_record(path) for path in paths]
    compute_related(records)

    for record in records:
        if record["filename"] == "0001-account-management.md" and not args.include_0001:
            continue
        rewrite_record(record, dry_run=args.dry_run)

    standardized = 0
    legacy = 0
    for path in paths:
        head = path.read_text(encoding="utf-8", errors="ignore")[:120]
        if head.startswith("---\n"):
            standardized += 1
        elif head.startswith(DASH_LINE):
            legacy += 1
    print(f"standardized={standardized} legacy={legacy}")


if __name__ == "__main__":
    main()
