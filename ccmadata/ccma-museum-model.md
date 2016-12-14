# ccma-objects_artists_exhibs.json

## Add Column

## Add Node/Literal
#### Literal Node: `aat:300266036`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `aat:300263534`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`

#### Literal Node: `aat:300312355`
Literal Type: `xsd:string`
<br/>Language: ``
<br/>isUri: `false`


## PyTransforms
#### _man_made_object_uri_
From column: _objects / Style_
``` python
return getValue("Style")
```

#### _Display_dimension_uri_
From column: _objects / Disp_Dimen_
``` python
return getValue("row_uri")+"/"+getValue("Disp_Dimen")
```

#### _MediumURI_
From column: _objects / Disp_Medium_
``` python
return UM.uri_from_fields("thesauri/medium/",getValue("Disp_Medium"))
```

#### _Disp_Title_URI_
From column: _objects / Disp_Title_
``` python
return UM.uri_from_fields("thesauri/title/",getValue("Disp_Title"))
```

#### _Department_URI_
From column: _objects / Department_
``` python
return UM.uri_from_fields("thesauri/department/",getValue("Department"))
```

#### _row_uri_
From column: _objects / embark_ID_
``` python
return "object/"+getValue("embark_ID")
```

#### _disp_access_no_uri_
From column: _objects / Disp_Access_No_
``` python
return getValue("row_uri")+"/"+getValue("Disp_Access_No")
```

#### _disp_create_date_uri_
From column: _objects / Disp_Create_DT_
``` python
return getValue("row_uri")+"/"+getValue("Disp_Create_DT")
```

#### _disp_obj_type_uri_
From column: _objects / Disp_Obj_Type_
``` python
return UM.uri_from_fields("thesauri/object_type/",getValue("Disp_Obj_Type"))
```

#### _artist_uri_
From column: _objects / Artist_Split / Values_
``` python
return UM.uri_from_fields("thesauri/artist/",getValue("Values"))
```

#### _imagepath_uri_
From column: _objects / Images / ImagePath_
``` python
return getValue("ImagePath")
```

#### _url_uri_
From column: _objects / URL_
``` python
return getValue("URL")
```


## Selections

## Semantic Types
| Column | Property | Class |
|  ----- | -------- | ----- |
| _Department_ | `rdfs:label` | `crm:E74_Group1`|
| _Department_URI_ | `uri` | `crm:E74_Group1`|
| _Disp_Access_No_ | `rdfs:label` | `crm:E42_Identifier1`|
| _Disp_Create_DT_ | `rdfs:label` | `crm:E52_Time-Span1`|
| _Disp_Dimen_ | `rdf:value` | `crm:E33_Linguistic_Object1`|
| _Disp_Medium_ | `skos:prefLabel` | `crm:E57_Material1`|
| _Disp_Obj_Type_ | `rdfs:label` | `crm:E55_Type2`|
| _Disp_Title_ | `crm:P2_has_type` | `crm:E35_Title1`|
| _Disp_Title_URI_ | `uri` | `crm:E35_Title1`|
| _Display_dimension_uri_ | `uri` | `crm:E33_Linguistic_Object1`|
| _ImagePath_ | `rdfs:label` | `crm:E38_Image1`|
| _Medium_ | `skos:prefLabel` | `crm:E57_Material2`|
| _MediumURI_ | `uri` | `crm:E57_Material1`|
| _URL_ | `rdfs:label` | `foaf:Document1`|
| _Values_ | `rdfs:label` | `crm:E39_Actor1`|
| __Disp_End_Date_ | `crm:P82b_end_of_the_end` | `crm:E52_Time-Span1`|
| __Disp_Start_Dat_ | `crm:P82a_begin_of_the_begin` | `crm:E52_Time-Span1`|
| _artist_uri_ | `uri` | `crm:E39_Actor1`|
| _disp_access_no_uri_ | `uri` | `crm:E42_Identifier1`|
| _disp_create_date_uri_ | `uri` | `crm:E52_Time-Span1`|
| _disp_obj_type_uri_ | `uri` | `crm:E55_Type2`|
| _imagepath_uri_ | `uri` | `crm:E38_Image1`|
| _row_uri_ | `uri` | `crm:E22_Man-Made_Object1`|
| _url_uri_ | `uri` | `foaf:Document1`|


## Links
| From | Property | To |
|  --- | -------- | ---|
| `crm:E12_Production1` | `crm:P14_carried_out_by` | `crm:E39_Actor1`|
| `crm:E12_Production1` | `crm:P4_has_time-span` | `crm:E52_Time-Span1`|
| `crm:E19_Physical_Object1` | `crm:P49_has_former_or_current_keeper` | `crm:E74_Group1`|
| `crm:E22_Man-Made_Object1` | `crm:P108i_was_produced_by` | `crm:E12_Production1`|
| `crm:E22_Man-Made_Object1` | `crm:P46i_forms_part_of` | `crm:E19_Physical_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P67i_is_referred_to_by` | `crm:E33_Linguistic_Object1`|
| `crm:E22_Man-Made_Object1` | `crm:P102_has_title` | `crm:E35_Title1`|
| `crm:E22_Man-Made_Object1` | `crm:P138i_has_representation` | `crm:E38_Image1`|
| `crm:E22_Man-Made_Object1` | `crm:P1_is_identified_by` | `crm:E42_Identifier1`|
| `crm:E22_Man-Made_Object1` | `crm:P2_has_type` | `crm:E55_Type2`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material1`|
| `crm:E22_Man-Made_Object1` | `crm:P45_consists_of` | `crm:E57_Material2`|
| `crm:E22_Man-Made_Object1` | `foaf:homepage` | `foaf:Document1`|
| `crm:E33_Linguistic_Object1` | `crm:P2_has_type` | `xsd:aat:300266036`|
| `crm:E42_Identifier1` | `crm:P2_has_type` | `xsd:aat:300312355`|
| `crm:E74_Group1` | `crm:P2_has_type` | `xsd:aat:300263534`|