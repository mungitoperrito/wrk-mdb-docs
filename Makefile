GIT_BRANCH=`git rev-parse --abbrev-ref HEAD`
USER=`whoami`
STAGING_URL="https://docs-mongodborg-staging.corp.mongodb.com"
PRODUCTION_URL="https://docs.mongodb.org"
STAGING_BUCKET=docs-mongodb-org-staging
PRODUCTION_BUCKET=docs-mongodb-org-prod

# "PROJECT" currently exists to support having multiple projects
# within one bucket. For the manual it is empty.
PROJECT=

.PHONY: help lint html stage deploy

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo
	@echo 'Variables'
	@printf "  \033[36m%-18s\033[0m %s\n" 'ARGS' 'Arguments to pass to mut-publish'

html: ## Builds this branch's HTML under build/<branch>/html
	giza make html

lint: ## Checks URLs in the built corpus underneath build/<branch>/html
	mut-lint --linters=links ./build/master/source/ ${ARGS}

# - Enter build/<branch>/html, and recurse over each regular file
#   <basename>/<filename>.
#   * Upload each to the S3 bucket under <project>/<username>/<basename>/<filename>
stage: ## Host online for review
	mut-publish build/${GIT_BRANCH}/html ${STAGING_BUCKET} --prefix=${PROJECT} --stage ${ARGS}
	@echo "Hosted at ${STAGING_URL}/${USER}/${GIT_BRANCH}/index.html"

# - Enter build/public/<branch>, as well as any symbolic links pointing
#   to it, and recurse over each file <basename>/<filename>.
#   * Upload each to the S3 bucket under <project>/<basename>/<filename>.
# - Upload each *regular file* <filename> underneath build/public
#   underneath <project>/<filename>.
# - Download the redirect rules from S3 that begin with one of the
#   --redirect-prefix regex rules.
# - Parse the file build/public/.htaccess, and for each redirect rule:
#   * If rule does not exist in remote set, upload redirect.
# - Remove previously-matched redirect rules in S3 that do not exist in
#   local redirect set.

# The recursive behavior would CHANGE if --all-subdirectories were
# given: ALL contents of build/public/<branch> would be upload
deploy: build/public ## Deploy to the production bucket
	@echo "Doing a dry-run"
	mut-publish build/public ${PRODUCTION_BUCKET} --prefix=${PROJECT} --deploy --redirect-prefix='v[0-9]\.[0-9]' --redirect-prefix='manual' --redirect-prefix='master' --verbose --dry-run ${ARGS}

	@echo 'Press any key to perform the previous' && read result
	mut-publish build/public ${PRODUCTION_BUCKET} --prefix=${PROJECT} --deploy --redirect-prefix='v[0-9]\.[0-9]' --redirect-prefix='manual' --redirect-prefix='master' ${ARGS}

	@echo "Hosted at ${PRODUCTION_URL}/index.html"
