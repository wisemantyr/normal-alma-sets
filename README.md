# normal-alma-sets
This repository contains python and VBA scripts for normalizing exported sets of items from [Alma Library Services Platform](https://exlibrisgroup.com/products/alma-library-services-platform/) to create reports of lost and missing items that can be shared with other library employees who do not use Alma.

Alma [sets](https://knowledge.exlibrisgroup.com/Alma/Product_Documentation/010Alma_Online_Help_(English)/050Administration/070Managing_Jobs/060Managing_Search_Queries_and_Sets) can be itemized or logical. The items in a set can be exported as an Excel sheet.

The normalization.py script is intended to be run on the exported results of a logical set. A logical set is essentially a saved search query. The parameters I have used for lost items at my library are:

```Physical Items```

where ```Base Status``` Equals ```Not in Place```

```Current Location``` Contains Phrase ```{Library Name}: {list of locations you want to monitor}```

```Tag Suppressed (Holdings)``` Equals ```No```

and ```Process Type``` Equals ```Lost```

The results are exported to results.xlsx. Then the normalization.py script is run to edit the available columns and column names, use regular expression to extract the Author from the "Type / Creator / Imprint" field, and filter items by date for monthly reports.

These reports allow information across departments to be centralized and allow for easy collection of simple statistics about item investigations



## Available search set fields
Formatting key:

**unique to search and/or necessary**

*possibly helpful and/or uncertain if repetitive values in other searches*

#### Physical items Search
- **Type / Creator / Imprint**
- **Barcode**
- Inventory Number
- Receiving Number
- Library
- Library Unit
- Temporary Library
- Creation Date
- **Modification Date**
- **Process type**
- To Library
- Expected Arrival Time
- At Library
- At
- On Hold Expiration Date
- Due Date
- Needed By
- Until
- **Permanent Location**
- **Temporary Location**
- **Call Number**
- Call Number Type
- Accession Number
- Temporary Call Number
- Item call number
- Item call number type
- **Status**
- RFID Security Status
- Due back
- **Item Policy**
- Temporary Item Policy
- **Material Type**
- **Copy ID**
- **Description**
- **Orders**
- **Requests**
- Peer Reviewed
- Item ID
- Holdings ID
- **MMS ID**

#### Physical titles Search
- Type / Creator / Imprint
- Subject
- Series
- Modification Date
- Creation Date
- Relation
- *Edition*
- *Medium Type*
- Language
- Language of Cataloging
- **ISBN**
- ISBN (13)
- Record number
- *Orders*
- *Requests*
- Peer Reviewed
- *MMS ID*

#### All titles Search
- Type / Creator / Imprint
- Subject
- Series
- Relation
- Creation Date
- Modification Date
- *Edition*
- **Uniform Title**
- *Medium Type*
- Language
- **Open Access**
- Language of Cataloging
- ISBN
- ISBN (13)
- ISSN
- Record Number
- *Orders*
- Peer Reviewed
- Managed by
- *Requests*
- *MMS ID*
