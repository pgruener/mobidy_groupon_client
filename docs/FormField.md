# FormField

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | id of this question. This is &#x60;required&#x60; only for the top level question, ie not required for question within the nested *fields* property. | [optional] 
**fields** | [**list[FormFieldFields]**](FormFieldFields.md) | This specifies the fields which are grouped together. A group may contain zero-to-many child groups, and there is no limit to how many times this nesting can occur. This is &#x60;required&#x60; for a field of *type* &#x60;GROUP&#x60;, as it specifies the fields within a group. A non-group field may contain zero-to-many fields. This data structure is used to support UI controls such as radio buttons or drop downs (using the &#x60;TEXT&#x60; *type*). A non-group field cannot have nested fields under these *fields*, nor may it contain &#x60;GROUP&#x60; *type* fields (i.e. a non-group field must have a flat list of child fields). Additionally, the child fields must have the same *property* as their parent field, and they must also have a *value*. | [optional] 
**hint** | **str** | Specifies a short hint that describes the expected value for this field. This may be used by a client to render a hint or placeholder value inside of an input field. | [optional] 
**label** | **str** | The label value to display for this checkout field. | [optional] 
**type** | **str** | Enum of field types | 
**value** | **str** | The default value the client should use to populate this checkout field. For &#x60;BOOLEAN&#x60; types, this will be normalized to true or false when outputting the fields and will not be null. If the value is true, then it is recommended to display the UI control in the “on” state (e.g. checked for a checkbox or enabled for a toggle). For a &#x60;TEXT&#x60; type with child fields, this will indicate the selected or default value. This can be used to populate the UI control with a pre-selected value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

