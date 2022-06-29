import os

FLE_2 = "-fle-2"
BUILD_DIR = "build"
PYTHON = "python"
PYTHON_FLE_2 = f"python{FLE_2}"
JAVA = "java"
JAVA_FLE_2 = f"java{FLE_2}"
CSHARP = "dotnet"
CSHARP_FLE_2 = f"dotnet{FLE_2}"
NODE = "node"
NODE_FLE_2 = f"node{FLE_2}"
DEK = "dek"
GO = "go"
GO_FLE_2 = f"go{FLE_2}"
FLE_2_LANGS = [NODE_FLE_2, PYTHON_FLE_2, GO_FLE_2, JAVA_FLE_2, CSHARP_FLE_2]
FLE_1_LANGS = [NODE, PYTHON, GO, JAVA, CSHARP]

INSERT = "insert"
EXTRA_FILES = "extra_files"
FORMAT_COMMAND = "format"
FILE_MAP = {
    PYTHON: {
        DEK: "make_data_key.py",
        INSERT: "insert_encrypted_document.py",
        EXTRA_FILES: ["requirements.txt"],
        FORMAT_COMMAND: f"black {os.path.join(BUILD_DIR,'*','*','*','*.py')}",
    },
    PYTHON_FLE_2: {
        DEK: "make_data_key.py",
        INSERT: "insert_encrypted_document.py",
        EXTRA_FILES: ["requirements.sh"],
        FORMAT_COMMAND: f"black {os.path.join(BUILD_DIR,'*','*','*','*.py')}",
    },
    JAVA: {
        DEK: os.path.join(
            "src", "main", "java", "com", "mongodb", "csfle", "makeDataKey.java"
        ),
        INSERT: os.path.join(
            "src",
            "main",
            "java",
            "com",
            "mongodb",
            "csfle",
            "insertEncryptedDocument.java",
        ),
        EXTRA_FILES: ["pom.xml"],
    },
    JAVA_FLE_2: {
        DEK: os.path.join(
            "src", "main", "java", "com", "mongodb", "csfle", "makeDataKey.java"
        ),
        INSERT: os.path.join(
            "src",
            "main",
            "java",
            "com",
            "mongodb",
            "csfle",
            "insertEncryptedDocument.java",
        ),
        EXTRA_FILES: ["pom.xml"],
    },
    CSHARP: {
        DEK: "CSFLE/MakeDataKey.cs",
        INSERT: "CSFLE/InsertEncryptedDocument.cs",
        EXTRA_FILES: ["CSFLE/CSFLE.csproj", "CSFLE/Program.cs"],
        FORMAT_COMMAND: f'find ./{BUILD_DIR} -name "*.csproj" | xargs -n1 dotnet format',
    },
    CSHARP_FLE_2: {
        DEK: "CSFLE/MakeDataKey.cs",
        INSERT: "CSFLE/InsertEncryptedDocument.cs",
        EXTRA_FILES: ["CSFLE/CSFLE.csproj", "CSFLE/Program.cs"],
        FORMAT_COMMAND: f'find ./{BUILD_DIR} -name "*.csproj" | xargs -n1 dotnet format',
    },
    NODE: {
        DEK: "make_data_key.js",
        INSERT: "insert_encrypted_document.js",
        EXTRA_FILES: ["package.json"],
        FORMAT_COMMAND: f"prettier --write {BUILD_DIR}",
    },
    NODE_FLE_2: {
        DEK: "make_data_key.js",
        INSERT: "insert_encrypted_document.js",
        EXTRA_FILES: ["package.json"],
        FORMAT_COMMAND: f"prettier --write {BUILD_DIR}",
    },
    GO: {
        DEK: "make-data-key.go",
        INSERT: "insert-encrypted-document.go",
        EXTRA_FILES: ["go.mod", "main.go"],
        FORMAT_COMMAND: f"gofmt -l -w -s {BUILD_DIR}",
    },
    GO_FLE_2: {
        DEK: "make-data-key.go",
        INSERT: "insert-encrypted-document.go",
        EXTRA_FILES: ["go.mod", "main.go"],
        FORMAT_COMMAND: f"gofmt -l -w -s {BUILD_DIR}",
    },
}

DIR_SEPERATOR = "-"
PROD = f"{DIR_SEPERATOR}reader"
TEST = f"{DIR_SEPERATOR}test"
AWS_PROD = f"aws{PROD}"
AWS_TEST = f"aws{TEST}"
GCP_PROD = f"gcp{PROD}"
GCP_TEST = f"gcp{TEST}"
AZURE_PROD = f"azure{PROD}"
AZURE_TEST = f"azure{TEST}"
LOCAL_PROD = f"local{PROD}"
LOCAL_TEST = f"local{TEST}"
BUILD_STATES = [
    AWS_PROD,
    AWS_TEST,
    AZURE_PROD,
    AZURE_TEST,
    GCP_PROD,
    GCP_TEST,
    LOCAL_PROD,
    LOCAL_TEST,
]

MAKE_KEY = lambda project: FILE_MAP[project][DEK]
MAKE_INSERT = lambda project: FILE_MAP[project][INSERT]
GET_EXTRA_FILES = lambda project: FILE_MAP[project].get(EXTRA_FILES)
BUILD_FILES = (MAKE_KEY, MAKE_INSERT)

BLUEHAWK = "bluehawk"
BLUEHAWK_HELP = f"""Unable to find {BLUEHAWK}. Run
the following command to install {BLUEHAWK}:

npm install -g {BLUEHAWK}

"""
