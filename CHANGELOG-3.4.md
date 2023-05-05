# Changelog Lizmap 3.4 HI

## 3.4.6 - 2021-09-21

- Fix: issue during the installation of the ldapdao module. Upgrade it to 2.2.1
- Fix: export button allowed in filter data with form when format is ODS
- Fix: integer key column sorted as text in attribute table tool
- Fix: Editing
  - In case of more than one editable layers, when there is a filter by login (or by polygon) activated,
  some of the popup items could miss the pencil button to open the editing form. Corrected by requesting
  the editable features for all the editable layers of the displayed popup items, and not only the first.

## 3.4.5 - 2021-09-14

- Fix: multiple selection edition w/ text field. Values can be integer but also string
- UI: when dock is closed, show edition is pending with green background on dock button
- Fix: use IGN PLANIGNV2 with free and paid keys
- UI: replace dock close button text by icon. This makes it more clear the dock is closed but tool can remain active
- Translation: add Romanian for dataTables (contribution from @ygorigor)
- Create utils method to parse XML and get error parsing message
- Fix: Object of class LibXMLError could not be converted to string
- Fix: Log errors about loading QGIS Project and provides errors messages
- Fix: lizmapTiler log errors when loading WMS GetCapabilities

## 3.4.4 - 2021-06-17

- Fix: form's labels partially hidden when too long. A line break and a hyphen are now used when needed
- Fix: In QGIS 3.16, the host in datasource can be written between single quotes
- Display spinner and disable button while waiting for print.
- Fix: fields are correctly hidden when 'Do not expose via WFS' is set in QGIS >=3.16
- Fix: QGIS >= 3.16 datasource compatibility
- Fix: Pre-generated cache is not used since Lizmap 3.4.1
- Fix: links into mails for registration or password recovery
