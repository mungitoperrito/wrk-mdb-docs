Create a unique index on the ``keyAltNames`` field in your
``encryption.__keyVault`` collection.

.. include:: /includes/queryable-encryption/tab-note.rst

.. tabs-drivers::

   .. tab::
      :tabid: nodejs

      .. literalinclude:: /includes/sample_apps/csfle/build/node-fle-2/gcp/reader/make_data_key.js
         :start-after: start-create-index
         :end-before: end-create-index
         :caption: make_data_key.js
         :language: javascript
         :dedent:

   .. tab::
      :tabid: python

      .. literalinclude:: /includes/sample_apps/csfle/build/python-fle-2/gcp/reader/make_data_key.py
         :start-after: start-create-index
         :end-before: end-create-index
         :language: python
         :dedent:
         :caption: make_data_key.py

   .. tab::
      :tabid: java-sync

      .. literalinclude:: /includes/sample_apps/csfle/build/java-fle-2/gcp/reader/src/main/java/com/mongodb/csfle/makeDataKey.java
         :start-after: start-create-index
         :end-before: end-create-index
         :language: java
         :dedent:
         :caption: makeDataKey.java

   .. tab::
      :tabid: go

      .. literalinclude:: /includes/sample_apps/csfle/build/go-fle-2/gcp/reader/make-data-key.go
         :start-after: start-create-index
         :end-before: end-create-index
         :language: go
         :dedent:
         :caption: make-data-key.go

   .. tab::
      :tabid: csharp

      .. literalinclude:: /includes/sample_apps/csfle/build/dotnet-fle-2/gcp/reader/CSFLE/MakeDataKey.cs
         :start-after: start-create-index
         :end-before: end-create-index
         :language: csharp
         :dedent:
         :caption: MakeDataKey.cs
