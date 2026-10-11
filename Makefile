# FeROS Sources — local developer commands (GNU Make + Python 3.11+)
PYTHON ?= python
GH ?= gh

.PHONY: validate site clean release-status release-publish

validate:
	$(PYTHON) scripts/validate.py

site: validate
	$(PYTHON) scripts/build_site.py

clean:
	$(PYTHON) -c "import shutil; shutil.rmtree('dist', ignore_errors=True)"

release-status:
	$(PYTHON) scripts/release.py status

release-publish:
	$(PYTHON) scripts/release.py publish
