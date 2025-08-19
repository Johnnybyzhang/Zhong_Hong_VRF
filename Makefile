.PHONY: help fmt lint test audit run bench migrate migrate-rollback clean install-dev

# Default target
help:
	@echo "Available commands:"
	@echo "  fmt              - Format code with black and ruff --fix"
	@echo "  lint             - Run linting checks (ruff, black --check)"
	@echo "  test             - Run tests with pytest"
	@echo "  audit            - Run security audits (pip-audit, bandit)"
	@echo "  run              - Start Home Assistant development environment"
	@echo "  bench            - Run performance benchmarks"
	@echo "  migrate          - Run database migrations (placeholder)"
	@echo "  migrate-rollback - Rollback database migrations (placeholder)"
	@echo "  clean            - Clean up build artifacts and cache"
	@echo "  install-dev      - Install development dependencies"

# Code formatting
fmt:
	@echo "🎨 Formatting code..."
	black --target-version py311 --line-length 100 custom_components tests
	ruff check --fix custom_components tests

# Linting checks
lint:
	@echo "🔍 Running linting checks..."
	ruff check custom_components tests
	black --check --target-version py311 --line-length 100 custom_components tests
	@echo "✅ All linting checks passed!"

# Run tests
test:
	@echo "🧪 Running tests..."
	python -m pytest tests/ -v --tb=short
	@echo "✅ Tests completed!"

# Security audit
audit:
	@echo "🔒 Running security audit..."
	pip-audit --desc --fix-dry-run
	@if ! bandit -r custom_components -f json -o bandit-report.json; then \
		echo "⚠️  Bandit found issues, check bandit-report.json"; \
		exit 1; \
	fi
	@echo "✅ Security audit completed!"

# Start development environment
run:
	@echo "🏃 Starting Home Assistant development environment..."
	@if [ -f "scripts/develop" ]; then \
		./scripts/develop; \
	elif command -v docker >/dev/null 2>&1; then \
		echo "Using Docker for HA development..."; \
		docker run --rm -it -v $(PWD):/workspaces/integration -p 8123:8123 \
			mcr.microsoft.com/vscode/devcontainers/python:3.11; \
	else \
		echo "❌ No development environment available. Install Docker or create scripts/develop"; \
	fi

# Performance benchmarks
bench:
	@echo "📊 Running performance benchmarks..."
	python -m pytest tests/ -k "bench" --benchmark-json=benchmark-results.json || echo "ℹ️  No benchmark tests found"
	@echo "✅ Benchmarks completed!"

# Database migrations (placeholder)
migrate:
	@echo "🔄 Running migrations..."
	@echo "ℹ️  No migrations required for this integration"

# Rollback migrations (placeholder)
migrate-rollback:
	@echo "↩️  Rolling back migrations..."
	@echo "ℹ️  No migrations to rollback for this integration"

# Clean up
clean:
	@echo "🧹 Cleaning up..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name ".pytest_cache" -delete
	rm -rf .coverage htmlcov/ .mypy_cache/ .ruff_cache/ build/ dist/ *.egg-info/
	rm -f bandit-report.json benchmark-results.json
	@echo "✅ Cleanup completed!"

# Install development dependencies
install-dev:
	@echo "📦 Installing development dependencies..."
	pip install black ruff pytest pytest-asyncio pytest-benchmark pip-audit bandit mypy
	@echo "✅ Development dependencies installed!"

# Pre-commit hook (run fmt, lint, test in sequence)
pre-commit: fmt lint test
	@echo "🚀 Pre-commit checks completed successfully!"
