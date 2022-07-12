These are the source files to build Dotnet sample
applications that use QE with the following KMS providers:

- AWS
- GCP
- Azure
- Local KMS

To build Dotnet applications, run the following command from the parent of this directory:

    python build.py --project dotnet-fle-2

To test your built applications, run the following
command from the parent of this directory:

    python -m unittest test.TestDotNetFLE2
