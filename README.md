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

These reports centralize information across departments and help gather statistics about item investigations.
