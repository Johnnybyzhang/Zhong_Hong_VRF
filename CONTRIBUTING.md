# Contributing to Zhong Hong VRF Integration

Thank you for your interest in contributing! This document outlines our development practices and quality standards.

## Development Setup

### Prerequisites

- Python 3.11+
- Home Assistant development environment  
- Git with conventional commit support

### Quick Start

1. **Clone and setup**:
   ```bash
   git clone https://github.com/Johnnybyzhang/home-assistant-zhong-hong.git
   cd home-assistant-zhong-hong
   make install-dev
   ```

2. **Run quality checks**:
   ```bash
   make fmt lint test
   ```

3. **Start development environment**:
   ```bash
   make run
   ```

## Code Quality Standards

### Linting and Formatting

- **Line length**: 100 characters maximum
- **Formatter**: Black with `skip-string-normalization = true`
- **Linter**: Ruff with Home Assistant rules enabled
- **Type checking**: mypy for static analysis

Run before committing:
```bash
make fmt      # Auto-fix formatting and import issues
make lint     # Check for style/logic issues  
make test     # Verify all tests pass
```

### Code Organization

- **Functions**: ≤ 50 effective lines each
- **Files**: ≤ 400 lines unless architecturally justified
- **Modules**: Prefer pure functions, push I/O to edges
- **Dependencies**: Inject dependencies, avoid global state

### Testing Requirements

All changes must include appropriate tests:

- **Golden tests**: Expected behavior for normal inputs
- **Failure tests**: Error handling and edge cases  
- **Edge tests**: Boundary conditions and unusual scenarios

Target ≥95% code coverage for new features.

## Commit and PR Guidelines

### Branch Naming

Use descriptive prefixes:
- `feat/add-temperature-sensors` - New features
- `fix/connection-timeout-handling` - Bug fixes
- `chore/update-dependencies` - Maintenance
- `docs/improve-setup-guide` - Documentation

### Conventional Commits

Format: `type(scope): description`

**Types:**
- `feat` - New features or capabilities
- `fix` - Bug fixes  
- `chore` - Maintenance, dependencies, tooling
- `docs` - Documentation changes
- `test` - Test additions or modifications
- `refactor` - Code restructuring without feature changes

**Examples:**
```
feat(climate): add humidity control support
fix(config): handle connection timeout gracefully  
chore(deps): update ruff to v0.1.7
docs(readme): add troubleshooting section
```

### Pull Request Standards

**Size and Scope:**
- ≤ 300 lines of code changes per PR
- Single concern per PR (one feature/fix/change)
- No direct pushes to `main` branch

**PR Template Checklist:**
- [ ] Lint/format pass; CI green
- [ ] Tests added/updated and meaningful
- [ ] Security/dependency scans clean or justified
- [ ] Docs & ADR updated; Context7/Figma refs linked
- [ ] Observability hooks present (logging/metrics)
- [ ] Rollback plan documented
- [ ] Reviewer approval; squash-merge with conventional commit title

**Required Content:**
- **Context**: What problem does this solve?
- **Test Evidence**: Screenshots/logs showing it works
- **Breaking Changes**: Any compatibility impacts
- **Rollback Notes**: How to undo if needed
- **References**: Link issues, ADRs, external docs

## Architecture Decisions

For significant changes, create an ADR (Architecture Decision Record):

```bash
# Create new ADR
cp docs/adr-template.md docs/adr-YYYYMMDD-your-decision.md
```

**ADR Requirements** (10-15 lines each):
- **Context**: Current situation and constraints
- **Decision**: What you decided and why
- **Alternatives**: Other options considered
- **Consequences**: Positive/negative impacts

## Security and Dependencies

### Prohibited Items
- No secrets in code, tests, logs, or comments
- No PII in logs or error messages
- No direct dependencies on copyleft licenses

### Required Checks
- `pip-audit --audit-level=moderate` must pass
- `bandit` security scan must be clean
- All dependencies must have SPDX license identifiers

## Quality Assurance  

### Performance
- Baseline metrics required for I/O paths
- Any regression >10% must be justified
- Use `make bench` for performance testing

### Observability
- INFO logs for setup/teardown lifecycle
- WARN logs for retries and recoverable errors  
- ERROR logs with actionable context (no PII)
- Feature flag for telemetry: `HA_ZHVRF_TELEMETRY=off`

## Documentation Standards

### User Documentation
- Update README for new configuration options
- Include screenshots for UI changes
- Provide examples for complex setups
- Update removal/troubleshooting guides

### Developer Documentation  
- ADRs for architectural decisions
- Inline docstrings for public APIs
- Type hints for all function signatures
- Comments for complex business logic only

## Release Process

### Version Management
- Semantic versioning (MAJOR.MINOR.PATCH)
- Update CHANGELOG.md for each PR  
- Tag releases after quality gate passes

### Deployment
- Canary release for breaking changes
- Staged rollout via HACS channels
- Monitor issues during rollout phase
- Documented rollback procedures ready

## Getting Help

- **Issues**: Use GitHub issues for bugs/features
- **Questions**: Start with README and existing issues  
- **Security**: Report privately via email to maintainers
- **Code Review**: Request review from `@Johnnybyzhang`

## Recognition

Contributors will be acknowledged in:
- CHANGELOG.md for significant contributions
- README.md credits section
- Release notes for major features

Thank you for helping improve the Zhong Hong VRF integration! 🚀
