from pathlib import Path
import toml
import re


def find_pyproject(filepath):
    cwd = Path(filepath).absolute().parent
    if (cwd / "pyproject.toml").is_file():
        return cwd / "pyproject.toml"
    else:
        return find_pyproject(cwd)


def parse_pyproject():
    return toml.load(find_pyproject(__file__).open())


def list_settings(package):
    has_dunder = re.compile(r"__.*__")
    return {key: val for key, val, in package.__dict__.items() if (key.isupper() and not has_dunder.fullmatch(key))}


# #   PACKAGE DOCUMENTATION (for pypi)
# setup_author = ("Terminal Labs",)
# setup_author_email = ("solutions@terminallabs.com",)
# setup_license = "see LICENSE file"
# setup_url = "https://github.com/predicatestudio/predicate_templates"
# package_link = "src"

# #   ADDITIONAL CONFIG
# reponame = "code"
# SETUP_NAME = reponame
# EGG_NAME = SETUP_NAME.replace("_", "-")
# PAYLOADPATH = SITEPACKAGESPATH  # noqa: F841
# server_port = 5000
# socket_host = "0.0.0.0"
# PAYLOADPATH = resolve_payload_path(EGG_NAME, PROJECT_NAME)  # noqa: F821
# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")
# DB_URL = "postgresql+psycopg2://{user}:{pw}@{url}/{db}".format(
#     user=POSTGRES_USER, pw=POSTGRES_PW, url=POSTGRES_URL, db=POSTGRES_DB
# )
# MONGO_DB = PROJECT_NAME  # noqa: F821
# UPLOAD_FOLDER = "uploads"
# ALLOWED_EXTENSIONS = set(["txt", "pdf", "png", "jpg", "jpeg", "gif", "zip"])
# BASEDIR = os.path.abspath(os.path.dirname(__file__))
# ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
# TEMPLATE_DIR = os.path.join(PAYLOADPATH, "templates")
# STATIC_DIR = os.path.join(PAYLOADPATH, "static")
# PERSISTENT_WORKING_DIRS = "stub"
# CONFIG_DIC = {
#     "POSTGRES_URL": POSTGRES_URL,
#     "POSTGRES_USER": POSTGRES_USER,
#     "POSTGRES_PW": POSTGRES_PW,
#     "POSTGRES_DB": POSTGRES_DB,
# }
# tempfile.tempdir = TEMPDIR  # noqa: F821

# ##
FRAMEWORK_VERSION = "0.1.dev1"  # https://www.python.org/dev/peps/pep-0440/
PRINT_VERBOSITY = "high"
EXCLUDED_DIRS = [".DS_Store"]
TEMPDIR = ".tmp/scratch"
DIRS = [f"{TEMPDIR}"]
TEXTTABLE_STYLE = ["-", "|", "+", "-"]

# Minimum version for this package
# MINIMUM_PYTHON_VERSION = (3, 6, 0)

# GENERATED SETTINGS
# from pyproject.toml
pproj = parse_pyproject()
project = pproj["project"]

PROJ_NAME = project.get("name")
PROJ_VERSION = project.get("version")
PROJ_DESC = project.get("description")
PROJ_README = project.get("readme")
PROJ_MIN_PYTHON = project.get("requires-python")
PROJ_LICENSE = project.get("license")
PROJ_AUTH = project.get("authors")
PROJ_MAINT = project.get("maintainers")
PROJ_DEPS = project.get("dependencies")
MINIMUM_PYTHON_VERSION = PROJ_MIN_PYTHON
COV_CONFIG = pproj.get("tool", {}).get("pytest", {}).get("pytest-cov", {}).get("cov-config")

# locally derived
PROJ_DIR = Path(__file__).absolute().parent
