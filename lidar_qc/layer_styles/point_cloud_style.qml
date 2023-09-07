<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" minScale="0" simplifyDrawingHints="1" styleCategories="AllStyleCategories" maxScale="0" simplifyAlgorithm="0" symbologyReferenceScale="-1" simplifyMaxScale="1" version="3.24.0-Tisler" labelsEnabled="1" simplifyLocal="1" readOnly="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal mode="0" startField="" endField="" durationUnit="min" startExpression="" fixedDuration="0" durationField="" enabled="0" accumulate="0" limitMode="0" endExpression="">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <renderer-v2 forceraster="0" symbollevels="0" type="RuleRenderer" referencescale="-1" enableorderby="0">
    <rules key="{88024a02-4938-473a-b42d-50019216a826}">
      <rule scalemindenom="5000" key="{226e4a52-006b-4ec0-bccd-7a93d421ba5b}" filter=" &quot;is_in_supplied_tile_index&quot; ~ 'false'" symbol="0" label="Not in supplied index" scalemaxdenom="100000"/>
      <rule key="{dd432a2e-3d9e-41b3-a5e2-23d0240938ee}" filter=" &quot;fid&quot; " symbol="1" label="Tiles"/>
      <rule scalemindenom="5000" key="{9e4aebaf-e31b-4aa8-915b-0029d1869df4}" filter=" &quot;is_tiling_correct&quot; ~ 'false'" symbol="2" label="Incorrect tiling" scalemaxdenom="100000"/>
      <rule scalemindenom="5000" key="{37272c74-4314-4548-bcd4-0e0572c0aac4}" filter=" &quot;is_file_name_correct_tile&quot; ~ 'false'" symbol="3" label="Incorrect tile in file name" scalemaxdenom="100000"/>
      <rule scalemindenom="5000" key="{b803f6b4-1da1-4cdb-aab9-1a90687b25f9}" filter=" &quot;is_file_name_correct_format&quot; ~ 'false'" symbol="4" label="Incorrect file name format" scalemaxdenom="100000"/>
      <rule scalemindenom="5000" key="{3f41a9f4-55af-4ca6-a23f-e8a7dcff40b3}" filter=" &quot;is_projection_correct&quot; ~ 'false'" symbol="5" label="Incorrect projection" scalemaxdenom="100000"/>
      <rule key="{70a67567-6b43-45f5-bb0b-0f97400dcf90}" filter=" regexp_match( &quot;classifications&quot; ,'\\b1\\b')" symbol="6" label="Unclassified" checkstate="0"/>
      <rule key="{ce197d9a-698d-4f60-9052-1027df17073d}" filter=" regexp_match( &quot;classifications&quot;,'\\b2\\b')" symbol="7" label="Ground " checkstate="0"/>
      <rule key="{e6b8ec6c-7f4e-4af6-aff4-930e4783ca8a}" filter="regexp_match(&quot;classifications&quot;,'\\b3\\b')" symbol="8" label="Low Vegetation" checkstate="0"/>
      <rule key="{6aae47da-8dd6-488d-b330-64e1e50b4163}" filter="regexp_match(&quot;classifications&quot;, '\\b4\\b')" symbol="9" label="Medium Vegetation" checkstate="0"/>
      <rule key="{d37a11de-fed9-4e90-bc6b-cfc02494c94f}" filter="regexp_match(&quot;classifications&quot;, '\\b5\\b')" symbol="10" label="High Vegetation" checkstate="0"/>
      <rule key="{52084824-8cde-4bbb-af2e-499e6659f2d2}" filter="regexp_match(&quot;classifications&quot;,'\\b6\\b')" symbol="11" label="Buildings" checkstate="0"/>
      <rule key="{aed2b768-5c17-4f1b-b32b-4b6a4e3c29f1}" filter=" regexp_match(&quot;classifications&quot;,'\\b9\\b')" symbol="12" label="Water" checkstate="0"/>
      <rule key="{d9a54dee-c3a6-414f-bace-7c3888fffbfb}" filter=" regexp_match( &quot;classifications&quot;, '\\b7\\b.*\\b18\\b')" symbol="13" label="Noise" checkstate="0"/>
      <rule key="{2ae7d3e7-2890-47bf-973f-9c1101df5969}" filter=" regexp_match(  &quot;classifications&quot; , '\\b17\\b')" symbol="14" label="Bridge" checkstate="0"/>
      <rule key="{c57f10fc-b5d3-4646-a291-38349406d8fb}" filter=" &quot;overlap_flag&quot; is not NULL" symbol="15" label="Overlap" checkstate="0"/>
      <rule key="{478d74ec-548c-444a-a080-655523f1de18}" filter=" &quot;withheld_flag&quot; is not NULL" symbol="16" label="Withheld" checkstate="0"/>
    </rules>
    <symbols>
      <symbol name="0" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="219,219,219,255"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="247,247,247,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="219,219,219,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="247,247,247,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="255,255,255,0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="0,0,0,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="255,255,255,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="10" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="32,70,15,124"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="32,70,15,124" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="11" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="243,135,3,255"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="b_diagonal"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="243,135,3,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="b_diagonal" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="12" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="PointPatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="double" value="0"/>
            <Option name="clip_mode" type="QString" value="shape"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="displacement_x" type="QString" value="0"/>
            <Option name="displacement_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="displacement_x_unit" type="QString" value="MM"/>
            <Option name="displacement_y" type="QString" value="0"/>
            <Option name="displacement_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="displacement_y_unit" type="QString" value="MM"/>
            <Option name="distance_x" type="QString" value="3"/>
            <Option name="distance_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_x_unit" type="QString" value="MM"/>
            <Option name="distance_y" type="QString" value="3"/>
            <Option name="distance_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_y_unit" type="QString" value="MM"/>
            <Option name="offset_x" type="QString" value="0"/>
            <Option name="offset_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_x_unit" type="QString" value="MM"/>
            <Option name="offset_y" type="QString" value="0"/>
            <Option name="offset_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_y_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="random_deviation_x" type="QString" value="0"/>
            <Option name="random_deviation_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="random_deviation_x_unit" type="QString" value="MM"/>
            <Option name="random_deviation_y" type="QString" value="0"/>
            <Option name="random_deviation_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="random_deviation_y_unit" type="QString" value="MM"/>
            <Option name="seed" type="QString" value="8184460"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="shape" k="clip_mode"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="0" k="displacement_x"/>
          <prop v="3x:0,0,0,0,0,0" k="displacement_x_map_unit_scale"/>
          <prop v="MM" k="displacement_x_unit"/>
          <prop v="0" k="displacement_y"/>
          <prop v="3x:0,0,0,0,0,0" k="displacement_y_map_unit_scale"/>
          <prop v="MM" k="displacement_y_unit"/>
          <prop v="3" k="distance_x"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_x_map_unit_scale"/>
          <prop v="MM" k="distance_x_unit"/>
          <prop v="3" k="distance_y"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_y_map_unit_scale"/>
          <prop v="MM" k="distance_y_unit"/>
          <prop v="0" k="offset_x"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_x_map_unit_scale"/>
          <prop v="MM" k="offset_x_unit"/>
          <prop v="0" k="offset_y"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_y_map_unit_scale"/>
          <prop v="MM" k="offset_y_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="0" k="random_deviation_x"/>
          <prop v="3x:0,0,0,0,0,0" k="random_deviation_x_map_unit_scale"/>
          <prop v="MM" k="random_deviation_x_unit"/>
          <prop v="0" k="random_deviation_y"/>
          <prop v="3x:0,0,0,0,0,0" k="random_deviation_y_map_unit_scale"/>
          <prop v="MM" k="random_deviation_y_unit"/>
          <prop v="8184460" k="seed"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@12@0" force_rhr="0" clip_to_extent="1" type="marker" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
              <Option type="Map">
                <Option name="angle" type="QString" value="0"/>
                <Option name="cap_style" type="QString" value="square"/>
                <Option name="color" type="QString" value="35,12,240,255"/>
                <Option name="horizontal_anchor_point" type="QString" value="1"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="name" type="QString" value="circle"/>
                <Option name="offset" type="QString" value="0,0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="outline_color" type="QString" value="35,35,35,255"/>
                <Option name="outline_style" type="QString" value="no"/>
                <Option name="outline_width" type="QString" value="0"/>
                <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="outline_width_unit" type="QString" value="MM"/>
                <Option name="scale_method" type="QString" value="diameter"/>
                <Option name="size" type="QString" value="1"/>
                <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="size_unit" type="QString" value="MM"/>
                <Option name="vertical_anchor_point" type="QString" value="1"/>
              </Option>
              <prop v="0" k="angle"/>
              <prop v="square" k="cap_style"/>
              <prop v="35,12,240,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="1" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="0,0,255,0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="0,0,255,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="13" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="PointPatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="double" value="0"/>
            <Option name="clip_mode" type="QString" value="shape"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="displacement_x" type="QString" value="0"/>
            <Option name="displacement_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="displacement_x_unit" type="QString" value="MM"/>
            <Option name="displacement_y" type="QString" value="0"/>
            <Option name="displacement_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="displacement_y_unit" type="QString" value="MM"/>
            <Option name="distance_x" type="QString" value="4"/>
            <Option name="distance_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_x_unit" type="QString" value="MM"/>
            <Option name="distance_y" type="QString" value="4"/>
            <Option name="distance_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_y_unit" type="QString" value="MM"/>
            <Option name="offset_x" type="QString" value="0"/>
            <Option name="offset_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_x_unit" type="QString" value="MM"/>
            <Option name="offset_y" type="QString" value="0"/>
            <Option name="offset_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_y_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="random_deviation_x" type="QString" value="0"/>
            <Option name="random_deviation_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="random_deviation_x_unit" type="QString" value="MM"/>
            <Option name="random_deviation_y" type="QString" value="0"/>
            <Option name="random_deviation_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="random_deviation_y_unit" type="QString" value="MM"/>
            <Option name="seed" type="QString" value="517945370"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="shape" k="clip_mode"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="0" k="displacement_x"/>
          <prop v="3x:0,0,0,0,0,0" k="displacement_x_map_unit_scale"/>
          <prop v="MM" k="displacement_x_unit"/>
          <prop v="0" k="displacement_y"/>
          <prop v="3x:0,0,0,0,0,0" k="displacement_y_map_unit_scale"/>
          <prop v="MM" k="displacement_y_unit"/>
          <prop v="4" k="distance_x"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_x_map_unit_scale"/>
          <prop v="MM" k="distance_x_unit"/>
          <prop v="4" k="distance_y"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_y_map_unit_scale"/>
          <prop v="MM" k="distance_y_unit"/>
          <prop v="0" k="offset_x"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_x_map_unit_scale"/>
          <prop v="MM" k="offset_x_unit"/>
          <prop v="0" k="offset_y"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_y_map_unit_scale"/>
          <prop v="MM" k="offset_y_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="0" k="random_deviation_x"/>
          <prop v="3x:0,0,0,0,0,0" k="random_deviation_x_map_unit_scale"/>
          <prop v="MM" k="random_deviation_x_unit"/>
          <prop v="0" k="random_deviation_y"/>
          <prop v="3x:0,0,0,0,0,0" k="random_deviation_y_map_unit_scale"/>
          <prop v="MM" k="random_deviation_y_unit"/>
          <prop v="517945370" k="seed"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@13@0" force_rhr="0" clip_to_extent="1" type="marker" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
              <Option type="Map">
                <Option name="angle" type="QString" value="0"/>
                <Option name="cap_style" type="QString" value="square"/>
                <Option name="color" type="QString" value="210,0,9,255"/>
                <Option name="horizontal_anchor_point" type="QString" value="1"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="name" type="QString" value="circle"/>
                <Option name="offset" type="QString" value="0,0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="outline_color" type="QString" value="35,35,35,255"/>
                <Option name="outline_style" type="QString" value="no"/>
                <Option name="outline_width" type="QString" value="0"/>
                <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="outline_width_unit" type="QString" value="MM"/>
                <Option name="scale_method" type="QString" value="diameter"/>
                <Option name="size" type="QString" value="1"/>
                <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="size_unit" type="QString" value="MM"/>
                <Option name="vertical_anchor_point" type="QString" value="2"/>
              </Option>
              <prop v="0" k="angle"/>
              <prop v="square" k="cap_style"/>
              <prop v="210,0,9,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="no" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="1" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="2" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="0,0,255,0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="0,0,255,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="14" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="LinePatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="QString" value="45"/>
            <Option name="clip_mode" type="QString" value="during_render"/>
            <Option name="color" type="QString" value="55,126,184,255"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="distance" type="QString" value="2"/>
            <Option name="distance_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_unit" type="QString" value="MM"/>
            <Option name="line_width" type="QString" value="0.26"/>
            <Option name="line_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
          </Option>
          <prop v="45" k="angle"/>
          <prop v="during_render" k="clip_mode"/>
          <prop v="55,126,184,255" k="color"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="2" k="distance"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="0.26" k="line_width"/>
          <prop v="3x:0,0,0,0,0,0" k="line_width_map_unit_scale"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@14@0" force_rhr="0" clip_to_extent="1" type="line" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleLine" enabled="1" pass="0">
              <Option type="Map">
                <Option name="align_dash_pattern" type="QString" value="0"/>
                <Option name="capstyle" type="QString" value="square"/>
                <Option name="customdash" type="QString" value="5;2"/>
                <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="customdash_unit" type="QString" value="MM"/>
                <Option name="dash_pattern_offset" type="QString" value="0"/>
                <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
                <Option name="draw_inside_polygon" type="QString" value="0"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="line_color" type="QString" value="0,0,0,255"/>
                <Option name="line_style" type="QString" value="solid"/>
                <Option name="line_width" type="QString" value="0.3"/>
                <Option name="line_width_unit" type="QString" value="MM"/>
                <Option name="offset" type="QString" value="0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="ring_filter" type="QString" value="0"/>
                <Option name="trim_distance_end" type="QString" value="0"/>
                <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_end_unit" type="QString" value="MM"/>
                <Option name="trim_distance_start" type="QString" value="0"/>
                <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_start_unit" type="QString" value="MM"/>
                <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
                <Option name="use_custom_dash" type="QString" value="0"/>
                <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              </Option>
              <prop v="0" k="align_dash_pattern"/>
              <prop v="square" k="capstyle"/>
              <prop v="5;2" k="customdash"/>
              <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
              <prop v="MM" k="customdash_unit"/>
              <prop v="0" k="dash_pattern_offset"/>
              <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
              <prop v="MM" k="dash_pattern_offset_unit"/>
              <prop v="0" k="draw_inside_polygon"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0,0,255" k="line_color"/>
              <prop v="solid" k="line_style"/>
              <prop v="0.3" k="line_width"/>
              <prop v="MM" k="line_width_unit"/>
              <prop v="0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0" k="ring_filter"/>
              <prop v="0" k="trim_distance_end"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
              <prop v="MM" k="trim_distance_end_unit"/>
              <prop v="0" k="trim_distance_start"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
              <prop v="MM" k="trim_distance_start_unit"/>
              <prop v="0" k="tweak_dash_pattern_on_corners"/>
              <prop v="0" k="use_custom_dash"/>
              <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="LinePatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="QString" value="135"/>
            <Option name="clip_mode" type="QString" value="during_render"/>
            <Option name="color" type="QString" value="55,126,184,255"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="distance" type="QString" value="2"/>
            <Option name="distance_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_unit" type="QString" value="MM"/>
            <Option name="line_width" type="QString" value="0.26"/>
            <Option name="line_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
          </Option>
          <prop v="135" k="angle"/>
          <prop v="during_render" k="clip_mode"/>
          <prop v="55,126,184,255" k="color"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="2" k="distance"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="0.26" k="line_width"/>
          <prop v="3x:0,0,0,0,0,0" k="line_width_map_unit_scale"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@14@1" force_rhr="0" clip_to_extent="1" type="line" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleLine" enabled="1" pass="0">
              <Option type="Map">
                <Option name="align_dash_pattern" type="QString" value="0"/>
                <Option name="capstyle" type="QString" value="square"/>
                <Option name="customdash" type="QString" value="5;2"/>
                <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="customdash_unit" type="QString" value="MM"/>
                <Option name="dash_pattern_offset" type="QString" value="0"/>
                <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
                <Option name="draw_inside_polygon" type="QString" value="0"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="line_color" type="QString" value="0,0,0,255"/>
                <Option name="line_style" type="QString" value="solid"/>
                <Option name="line_width" type="QString" value="0.3"/>
                <Option name="line_width_unit" type="QString" value="MM"/>
                <Option name="offset" type="QString" value="0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="ring_filter" type="QString" value="0"/>
                <Option name="trim_distance_end" type="QString" value="0"/>
                <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_end_unit" type="QString" value="MM"/>
                <Option name="trim_distance_start" type="QString" value="0"/>
                <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_start_unit" type="QString" value="MM"/>
                <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
                <Option name="use_custom_dash" type="QString" value="0"/>
                <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              </Option>
              <prop v="0" k="align_dash_pattern"/>
              <prop v="square" k="capstyle"/>
              <prop v="5;2" k="customdash"/>
              <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
              <prop v="MM" k="customdash_unit"/>
              <prop v="0" k="dash_pattern_offset"/>
              <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
              <prop v="MM" k="dash_pattern_offset_unit"/>
              <prop v="0" k="draw_inside_polygon"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0,0,255" k="line_color"/>
              <prop v="solid" k="line_style"/>
              <prop v="0.3" k="line_width"/>
              <prop v="MM" k="line_width_unit"/>
              <prop v="0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0" k="ring_filter"/>
              <prop v="0" k="trim_distance_end"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
              <prop v="MM" k="trim_distance_end_unit"/>
              <prop v="0" k="trim_distance_start"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
              <prop v="MM" k="trim_distance_start_unit"/>
              <prop v="0" k="tweak_dash_pattern_on_corners"/>
              <prop v="0" k="use_custom_dash"/>
              <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
          <Option type="Map">
            <Option name="align_dash_pattern" type="QString" value="0"/>
            <Option name="capstyle" type="QString" value="square"/>
            <Option name="customdash" type="QString" value="5;2"/>
            <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="customdash_unit" type="QString" value="MM"/>
            <Option name="dash_pattern_offset" type="QString" value="0"/>
            <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
            <Option name="draw_inside_polygon" type="QString" value="0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="line_color" type="QString" value="0,0,0,255"/>
            <Option name="line_style" type="QString" value="solid"/>
            <Option name="line_width" type="QString" value="0.3"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="ring_filter" type="QString" value="0"/>
            <Option name="trim_distance_end" type="QString" value="0"/>
            <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_end_unit" type="QString" value="MM"/>
            <Option name="trim_distance_start" type="QString" value="0"/>
            <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_start_unit" type="QString" value="MM"/>
            <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
            <Option name="use_custom_dash" type="QString" value="0"/>
            <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,0,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.3" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="15" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="243,166,178,255"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="243,166,178,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="16" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="114,155,111,255"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="114,155,111,255" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
          <Option type="Map">
            <Option name="align_dash_pattern" type="QString" value="0"/>
            <Option name="capstyle" type="QString" value="square"/>
            <Option name="customdash" type="QString" value="5;2"/>
            <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="customdash_unit" type="QString" value="MM"/>
            <Option name="dash_pattern_offset" type="QString" value="0"/>
            <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
            <Option name="draw_inside_polygon" type="QString" value="0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="line_color" type="QString" value="228,26,28,255"/>
            <Option name="line_style" type="QString" value="solid"/>
            <Option name="line_width" type="QString" value="0.46"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="ring_filter" type="QString" value="0"/>
            <Option name="trim_distance_end" type="QString" value="0"/>
            <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_end_unit" type="QString" value="MM"/>
            <Option name="trim_distance_start" type="QString" value="0"/>
            <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_start_unit" type="QString" value="MM"/>
            <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
            <Option name="use_custom_dash" type="QString" value="0"/>
            <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="228,26,28,255" k="line_color"/>
          <prop v="solid" k="line_style"/>
          <prop v="0.46" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="3" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="LinePatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="QString" value="135"/>
            <Option name="clip_mode" type="QString" value="during_render"/>
            <Option name="color" type="QString" value="55,126,184,255"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="distance" type="QString" value="4"/>
            <Option name="distance_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_unit" type="QString" value="MM"/>
            <Option name="line_width" type="QString" value="0.26"/>
            <Option name="line_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
          </Option>
          <prop v="135" k="angle"/>
          <prop v="during_render" k="clip_mode"/>
          <prop v="55,126,184,255" k="color"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="4" k="distance"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="0.26" k="line_width"/>
          <prop v="3x:0,0,0,0,0,0" k="line_width_map_unit_scale"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@3@0" force_rhr="0" clip_to_extent="1" type="line" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleLine" enabled="1" pass="0">
              <Option type="Map">
                <Option name="align_dash_pattern" type="QString" value="0"/>
                <Option name="capstyle" type="QString" value="square"/>
                <Option name="customdash" type="QString" value="5;2"/>
                <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="customdash_unit" type="QString" value="MM"/>
                <Option name="dash_pattern_offset" type="QString" value="0"/>
                <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
                <Option name="draw_inside_polygon" type="QString" value="0"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="line_color" type="QString" value="0,0,159,255"/>
                <Option name="line_style" type="QString" value="solid"/>
                <Option name="line_width" type="QString" value="0.3"/>
                <Option name="line_width_unit" type="QString" value="MM"/>
                <Option name="offset" type="QString" value="0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="ring_filter" type="QString" value="0"/>
                <Option name="trim_distance_end" type="QString" value="0"/>
                <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_end_unit" type="QString" value="MM"/>
                <Option name="trim_distance_start" type="QString" value="0"/>
                <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_start_unit" type="QString" value="MM"/>
                <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
                <Option name="use_custom_dash" type="QString" value="0"/>
                <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              </Option>
              <prop v="0" k="align_dash_pattern"/>
              <prop v="square" k="capstyle"/>
              <prop v="5;2" k="customdash"/>
              <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
              <prop v="MM" k="customdash_unit"/>
              <prop v="0" k="dash_pattern_offset"/>
              <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
              <prop v="MM" k="dash_pattern_offset_unit"/>
              <prop v="0" k="draw_inside_polygon"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0,159,255" k="line_color"/>
              <prop v="solid" k="line_style"/>
              <prop v="0.3" k="line_width"/>
              <prop v="MM" k="line_width_unit"/>
              <prop v="0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0" k="ring_filter"/>
              <prop v="0" k="trim_distance_end"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
              <prop v="MM" k="trim_distance_end_unit"/>
              <prop v="0" k="trim_distance_start"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
              <prop v="MM" k="trim_distance_start_unit"/>
              <prop v="0" k="tweak_dash_pattern_on_corners"/>
              <prop v="0" k="use_custom_dash"/>
              <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
          <Option type="Map">
            <Option name="align_dash_pattern" type="QString" value="0"/>
            <Option name="capstyle" type="QString" value="square"/>
            <Option name="customdash" type="QString" value="5;2"/>
            <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="customdash_unit" type="QString" value="MM"/>
            <Option name="dash_pattern_offset" type="QString" value="0"/>
            <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
            <Option name="draw_inside_polygon" type="QString" value="0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="line_color" type="QString" value="0,0,0,255"/>
            <Option name="line_style" type="QString" value="no"/>
            <Option name="line_width" type="QString" value="0.46"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="ring_filter" type="QString" value="0"/>
            <Option name="trim_distance_end" type="QString" value="0"/>
            <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_end_unit" type="QString" value="MM"/>
            <Option name="trim_distance_start" type="QString" value="0"/>
            <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_start_unit" type="QString" value="MM"/>
            <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
            <Option name="use_custom_dash" type="QString" value="0"/>
            <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,0,255" k="line_color"/>
          <prop v="no" k="line_style"/>
          <prop v="0.46" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="LinePatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="QString" value="45"/>
            <Option name="clip_mode" type="QString" value="during_render"/>
            <Option name="color" type="QString" value="55,126,184,255"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="distance" type="QString" value="4"/>
            <Option name="distance_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_unit" type="QString" value="MM"/>
            <Option name="line_width" type="QString" value="0.26"/>
            <Option name="line_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
          </Option>
          <prop v="45" k="angle"/>
          <prop v="during_render" k="clip_mode"/>
          <prop v="55,126,184,255" k="color"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="4" k="distance"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="0.26" k="line_width"/>
          <prop v="3x:0,0,0,0,0,0" k="line_width_map_unit_scale"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@4@0" force_rhr="0" clip_to_extent="1" type="line" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleLine" enabled="1" pass="0">
              <Option type="Map">
                <Option name="align_dash_pattern" type="QString" value="0"/>
                <Option name="capstyle" type="QString" value="square"/>
                <Option name="customdash" type="QString" value="5;2"/>
                <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="customdash_unit" type="QString" value="MM"/>
                <Option name="dash_pattern_offset" type="QString" value="0"/>
                <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
                <Option name="draw_inside_polygon" type="QString" value="0"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="line_color" type="QString" value="0,127,0,255"/>
                <Option name="line_style" type="QString" value="solid"/>
                <Option name="line_width" type="QString" value="0.3"/>
                <Option name="line_width_unit" type="QString" value="MM"/>
                <Option name="offset" type="QString" value="0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="ring_filter" type="QString" value="0"/>
                <Option name="trim_distance_end" type="QString" value="0"/>
                <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_end_unit" type="QString" value="MM"/>
                <Option name="trim_distance_start" type="QString" value="0"/>
                <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_start_unit" type="QString" value="MM"/>
                <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
                <Option name="use_custom_dash" type="QString" value="0"/>
                <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              </Option>
              <prop v="0" k="align_dash_pattern"/>
              <prop v="square" k="capstyle"/>
              <prop v="5;2" k="customdash"/>
              <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
              <prop v="MM" k="customdash_unit"/>
              <prop v="0" k="dash_pattern_offset"/>
              <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
              <prop v="MM" k="dash_pattern_offset_unit"/>
              <prop v="0" k="draw_inside_polygon"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,127,0,255" k="line_color"/>
              <prop v="solid" k="line_style"/>
              <prop v="0.3" k="line_width"/>
              <prop v="MM" k="line_width_unit"/>
              <prop v="0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0" k="ring_filter"/>
              <prop v="0" k="trim_distance_end"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
              <prop v="MM" k="trim_distance_end_unit"/>
              <prop v="0" k="trim_distance_start"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
              <prop v="MM" k="trim_distance_start_unit"/>
              <prop v="0" k="tweak_dash_pattern_on_corners"/>
              <prop v="0" k="use_custom_dash"/>
              <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
          <Option type="Map">
            <Option name="align_dash_pattern" type="QString" value="0"/>
            <Option name="capstyle" type="QString" value="square"/>
            <Option name="customdash" type="QString" value="5;2"/>
            <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="customdash_unit" type="QString" value="MM"/>
            <Option name="dash_pattern_offset" type="QString" value="0"/>
            <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
            <Option name="draw_inside_polygon" type="QString" value="0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="line_color" type="QString" value="0,0,0,255"/>
            <Option name="line_style" type="QString" value="no"/>
            <Option name="line_width" type="QString" value="0.46"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="ring_filter" type="QString" value="0"/>
            <Option name="trim_distance_end" type="QString" value="0"/>
            <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_end_unit" type="QString" value="MM"/>
            <Option name="trim_distance_start" type="QString" value="0"/>
            <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_start_unit" type="QString" value="MM"/>
            <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
            <Option name="use_custom_dash" type="QString" value="0"/>
            <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0,0,255" k="line_color"/>
          <prop v="no" k="line_style"/>
          <prop v="0.46" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="5" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="PointPatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="double" value="0"/>
            <Option name="clip_mode" type="QString" value="shape"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="displacement_x" type="QString" value="5"/>
            <Option name="displacement_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="displacement_x_unit" type="QString" value="MM"/>
            <Option name="displacement_y" type="QString" value="5"/>
            <Option name="displacement_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="displacement_y_unit" type="QString" value="MM"/>
            <Option name="distance_x" type="QString" value="15"/>
            <Option name="distance_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_x_unit" type="QString" value="MM"/>
            <Option name="distance_y" type="QString" value="15"/>
            <Option name="distance_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_y_unit" type="QString" value="MM"/>
            <Option name="offset_x" type="QString" value="0"/>
            <Option name="offset_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_x_unit" type="QString" value="MM"/>
            <Option name="offset_y" type="QString" value="0"/>
            <Option name="offset_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_y_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="random_deviation_x" type="QString" value="0"/>
            <Option name="random_deviation_x_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="random_deviation_x_unit" type="QString" value="MM"/>
            <Option name="random_deviation_y" type="QString" value="0"/>
            <Option name="random_deviation_y_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="random_deviation_y_unit" type="QString" value="MM"/>
            <Option name="seed" type="QString" value="626704236"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="shape" k="clip_mode"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="5" k="displacement_x"/>
          <prop v="3x:0,0,0,0,0,0" k="displacement_x_map_unit_scale"/>
          <prop v="MM" k="displacement_x_unit"/>
          <prop v="5" k="displacement_y"/>
          <prop v="3x:0,0,0,0,0,0" k="displacement_y_map_unit_scale"/>
          <prop v="MM" k="displacement_y_unit"/>
          <prop v="15" k="distance_x"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_x_map_unit_scale"/>
          <prop v="MM" k="distance_x_unit"/>
          <prop v="15" k="distance_y"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_y_map_unit_scale"/>
          <prop v="MM" k="distance_y_unit"/>
          <prop v="0" k="offset_x"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_x_map_unit_scale"/>
          <prop v="MM" k="offset_x_unit"/>
          <prop v="0" k="offset_y"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_y_map_unit_scale"/>
          <prop v="MM" k="offset_y_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="0" k="random_deviation_x"/>
          <prop v="3x:0,0,0,0,0,0" k="random_deviation_x_map_unit_scale"/>
          <prop v="MM" k="random_deviation_x_unit"/>
          <prop v="0" k="random_deviation_y"/>
          <prop v="3x:0,0,0,0,0,0" k="random_deviation_y_map_unit_scale"/>
          <prop v="MM" k="random_deviation_y_unit"/>
          <prop v="626704236" k="seed"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@5@0" force_rhr="0" clip_to_extent="1" type="marker" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
              <Option type="Map">
                <Option name="angle" type="QString" value="0"/>
                <Option name="cap_style" type="QString" value="square"/>
                <Option name="color" type="QString" value="219,128,0,255"/>
                <Option name="horizontal_anchor_point" type="QString" value="1"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="name" type="QString" value="circle"/>
                <Option name="offset" type="QString" value="0,0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="outline_color" type="QString" value="35,35,35,255"/>
                <Option name="outline_style" type="QString" value="solid"/>
                <Option name="outline_width" type="QString" value="0"/>
                <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="outline_width_unit" type="QString" value="MM"/>
                <Option name="scale_method" type="QString" value="diameter"/>
                <Option name="size" type="QString" value="1.5"/>
                <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="size_unit" type="QString" value="MM"/>
                <Option name="vertical_anchor_point" type="QString" value="1"/>
              </Option>
              <prop v="0" k="angle"/>
              <prop v="square" k="cap_style"/>
              <prop v="219,128,0,255" k="color"/>
              <prop v="1" k="horizontal_anchor_point"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="circle" k="name"/>
              <prop v="0,0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="35,35,35,255" k="outline_color"/>
              <prop v="solid" k="outline_style"/>
              <prop v="0" k="outline_width"/>
              <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
              <prop v="MM" k="outline_width_unit"/>
              <prop v="diameter" k="scale_method"/>
              <prop v="1.5" k="size"/>
              <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
              <prop v="MM" k="size_unit"/>
              <prop v="1" k="vertical_anchor_point"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleLine" enabled="1" pass="0">
          <Option type="Map">
            <Option name="align_dash_pattern" type="QString" value="0"/>
            <Option name="capstyle" type="QString" value="square"/>
            <Option name="customdash" type="QString" value="5;2"/>
            <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="customdash_unit" type="QString" value="MM"/>
            <Option name="dash_pattern_offset" type="QString" value="0"/>
            <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
            <Option name="draw_inside_polygon" type="QString" value="0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="line_color" type="QString" value="219,128,0,255"/>
            <Option name="line_style" type="QString" value="no"/>
            <Option name="line_width" type="QString" value="0.36"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="ring_filter" type="QString" value="0"/>
            <Option name="trim_distance_end" type="QString" value="0"/>
            <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_end_unit" type="QString" value="MM"/>
            <Option name="trim_distance_start" type="QString" value="0"/>
            <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="trim_distance_start_unit" type="QString" value="MM"/>
            <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
            <Option name="use_custom_dash" type="QString" value="0"/>
            <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          </Option>
          <prop v="0" k="align_dash_pattern"/>
          <prop v="square" k="capstyle"/>
          <prop v="5;2" k="customdash"/>
          <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
          <prop v="MM" k="customdash_unit"/>
          <prop v="0" k="dash_pattern_offset"/>
          <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
          <prop v="MM" k="dash_pattern_offset_unit"/>
          <prop v="0" k="draw_inside_polygon"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="219,128,0,255" k="line_color"/>
          <prop v="no" k="line_style"/>
          <prop v="0.36" k="line_width"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0" k="ring_filter"/>
          <prop v="0" k="trim_distance_end"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
          <prop v="MM" k="trim_distance_end_unit"/>
          <prop v="0" k="trim_distance_start"/>
          <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
          <prop v="MM" k="trim_distance_start_unit"/>
          <prop v="0" k="tweak_dash_pattern_on_corners"/>
          <prop v="0" k="use_custom_dash"/>
          <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="6" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="LinePatternFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="angle" type="QString" value="0"/>
            <Option name="clip_mode" type="QString" value="during_render"/>
            <Option name="color" type="QString" value="0,0,0,255"/>
            <Option name="coordinate_reference" type="QString" value="feature"/>
            <Option name="distance" type="QString" value="5"/>
            <Option name="distance_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="distance_unit" type="QString" value="MM"/>
            <Option name="line_width" type="QString" value="0.5"/>
            <Option name="line_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="line_width_unit" type="QString" value="MM"/>
            <Option name="offset" type="QString" value="0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
          </Option>
          <prop v="0" k="angle"/>
          <prop v="during_render" k="clip_mode"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="feature" k="coordinate_reference"/>
          <prop v="5" k="distance"/>
          <prop v="3x:0,0,0,0,0,0" k="distance_map_unit_scale"/>
          <prop v="MM" k="distance_unit"/>
          <prop v="0.5" k="line_width"/>
          <prop v="3x:0,0,0,0,0,0" k="line_width_map_unit_scale"/>
          <prop v="MM" k="line_width_unit"/>
          <prop v="0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <symbol name="@6@0" force_rhr="0" clip_to_extent="1" type="line" alpha="1">
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
            <layer locked="0" class="SimpleLine" enabled="1" pass="0">
              <Option type="Map">
                <Option name="align_dash_pattern" type="QString" value="0"/>
                <Option name="capstyle" type="QString" value="square"/>
                <Option name="customdash" type="QString" value="5;2"/>
                <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="customdash_unit" type="QString" value="MM"/>
                <Option name="dash_pattern_offset" type="QString" value="0"/>
                <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
                <Option name="draw_inside_polygon" type="QString" value="0"/>
                <Option name="joinstyle" type="QString" value="bevel"/>
                <Option name="line_color" type="QString" value="0,0,0,255"/>
                <Option name="line_style" type="QString" value="solid"/>
                <Option name="line_width" type="QString" value="0.25"/>
                <Option name="line_width_unit" type="QString" value="MM"/>
                <Option name="offset" type="QString" value="0"/>
                <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="offset_unit" type="QString" value="MM"/>
                <Option name="ring_filter" type="QString" value="0"/>
                <Option name="trim_distance_end" type="QString" value="0"/>
                <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_end_unit" type="QString" value="MM"/>
                <Option name="trim_distance_start" type="QString" value="0"/>
                <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                <Option name="trim_distance_start_unit" type="QString" value="MM"/>
                <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
                <Option name="use_custom_dash" type="QString" value="0"/>
                <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              </Option>
              <prop v="0" k="align_dash_pattern"/>
              <prop v="square" k="capstyle"/>
              <prop v="5;2" k="customdash"/>
              <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
              <prop v="MM" k="customdash_unit"/>
              <prop v="0" k="dash_pattern_offset"/>
              <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
              <prop v="MM" k="dash_pattern_offset_unit"/>
              <prop v="0" k="draw_inside_polygon"/>
              <prop v="bevel" k="joinstyle"/>
              <prop v="0,0,0,255" k="line_color"/>
              <prop v="solid" k="line_style"/>
              <prop v="0.25" k="line_width"/>
              <prop v="MM" k="line_width_unit"/>
              <prop v="0" k="offset"/>
              <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
              <prop v="MM" k="offset_unit"/>
              <prop v="0" k="ring_filter"/>
              <prop v="0" k="trim_distance_end"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
              <prop v="MM" k="trim_distance_end_unit"/>
              <prop v="0" k="trim_distance_start"/>
              <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
              <prop v="MM" k="trim_distance_start_unit"/>
              <prop v="0" k="tweak_dash_pattern_on_corners"/>
              <prop v="0" k="use_custom_dash"/>
              <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
              <data_defined_properties>
                <Option type="Map">
                  <Option name="name" type="QString" value=""/>
                  <Option name="properties"/>
                  <Option name="type" type="QString" value="collection"/>
                </Option>
              </data_defined_properties>
            </layer>
          </symbol>
        </layer>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="0,0,255,0"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="0,0,255,0" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="7" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="171,119,22,113"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="171,119,22,113" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="8" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="148,227,105,131"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.46"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="148,227,105,131" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.46" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="9" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
        <data_defined_properties>
          <Option type="Map">
            <Option name="name" type="QString" value=""/>
            <Option name="properties"/>
            <Option name="type" type="QString" value="collection"/>
          </Option>
        </data_defined_properties>
        <layer locked="0" class="SimpleFill" enabled="1" pass="0">
          <Option type="Map">
            <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="color" type="QString" value="113,180,50,160"/>
            <Option name="joinstyle" type="QString" value="bevel"/>
            <Option name="offset" type="QString" value="0,0"/>
            <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            <Option name="offset_unit" type="QString" value="MM"/>
            <Option name="outline_color" type="QString" value="35,35,35,255"/>
            <Option name="outline_style" type="QString" value="solid"/>
            <Option name="outline_width" type="QString" value="0.26"/>
            <Option name="outline_width_unit" type="QString" value="MM"/>
            <Option name="style" type="QString" value="solid"/>
          </Option>
          <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
          <prop v="113,180,50,160" k="color"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0.26" k="outline_width"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="solid" k="style"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <effect type="effectStack" enabled="0">
      <effect type="dropShadow">
        <Option type="Map">
          <Option name="blend_mode" type="QString" value="13"/>
          <Option name="blur_level" type="QString" value="2.545"/>
          <Option name="blur_unit" type="QString" value="MM"/>
          <Option name="blur_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="color" type="QString" value="12,12,12,255"/>
          <Option name="draw_mode" type="QString" value="2"/>
          <Option name="enabled" type="QString" value="1"/>
          <Option name="offset_angle" type="QString" value="135"/>
          <Option name="offset_distance" type="QString" value="0.5"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="offset_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="opacity" type="QString" value="1"/>
        </Option>
        <prop v="13" k="blend_mode"/>
        <prop v="2.545" k="blur_level"/>
        <prop v="MM" k="blur_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="blur_unit_scale"/>
        <prop v="12,12,12,255" k="color"/>
        <prop v="2" k="draw_mode"/>
        <prop v="1" k="enabled"/>
        <prop v="135" k="offset_angle"/>
        <prop v="0.5" k="offset_distance"/>
        <prop v="MM" k="offset_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
        <prop v="1" k="opacity"/>
      </effect>
      <effect type="outerGlow">
        <Option type="Map">
          <Option name="blend_mode" type="QString" value="0"/>
          <Option name="blur_level" type="QString" value="2.645"/>
          <Option name="blur_unit" type="QString" value="MM"/>
          <Option name="blur_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="color1" type="QString" value="69,116,40,255"/>
          <Option name="color2" type="QString" value="188,220,60,255"/>
          <Option name="color_type" type="QString" value="0"/>
          <Option name="direction" type="QString" value="ccw"/>
          <Option name="discrete" type="QString" value="0"/>
          <Option name="draw_mode" type="QString" value="2"/>
          <Option name="enabled" type="QString" value="0"/>
          <Option name="opacity" type="QString" value="0.5"/>
          <Option name="rampType" type="QString" value="gradient"/>
          <Option name="single_color" type="QString" value="255,255,255,255"/>
          <Option name="spec" type="QString" value="rgb"/>
          <Option name="spread" type="QString" value="2"/>
          <Option name="spread_unit" type="QString" value="MM"/>
          <Option name="spread_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
        </Option>
        <prop v="0" k="blend_mode"/>
        <prop v="2.645" k="blur_level"/>
        <prop v="MM" k="blur_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="blur_unit_scale"/>
        <prop v="69,116,40,255" k="color1"/>
        <prop v="188,220,60,255" k="color2"/>
        <prop v="0" k="color_type"/>
        <prop v="ccw" k="direction"/>
        <prop v="0" k="discrete"/>
        <prop v="2" k="draw_mode"/>
        <prop v="0" k="enabled"/>
        <prop v="0.5" k="opacity"/>
        <prop v="gradient" k="rampType"/>
        <prop v="255,255,255,255" k="single_color"/>
        <prop v="rgb" k="spec"/>
        <prop v="2" k="spread"/>
        <prop v="MM" k="spread_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="spread_unit_scale"/>
      </effect>
      <effect type="drawSource">
        <Option type="Map">
          <Option name="blend_mode" type="QString" value="0"/>
          <Option name="draw_mode" type="QString" value="2"/>
          <Option name="enabled" type="QString" value="1"/>
          <Option name="opacity" type="QString" value="0.918"/>
        </Option>
        <prop v="0" k="blend_mode"/>
        <prop v="2" k="draw_mode"/>
        <prop v="1" k="enabled"/>
        <prop v="0.918" k="opacity"/>
      </effect>
      <effect type="innerShadow">
        <Option type="Map">
          <Option name="blend_mode" type="QString" value="13"/>
          <Option name="blur_level" type="QString" value="2.645"/>
          <Option name="blur_unit" type="QString" value="MM"/>
          <Option name="blur_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="color" type="QString" value="0,0,0,255"/>
          <Option name="draw_mode" type="QString" value="2"/>
          <Option name="enabled" type="QString" value="0"/>
          <Option name="offset_angle" type="QString" value="135"/>
          <Option name="offset_distance" type="QString" value="2"/>
          <Option name="offset_unit" type="QString" value="MM"/>
          <Option name="offset_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="opacity" type="QString" value="1"/>
        </Option>
        <prop v="13" k="blend_mode"/>
        <prop v="2.645" k="blur_level"/>
        <prop v="MM" k="blur_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="blur_unit_scale"/>
        <prop v="0,0,0,255" k="color"/>
        <prop v="2" k="draw_mode"/>
        <prop v="0" k="enabled"/>
        <prop v="135" k="offset_angle"/>
        <prop v="2" k="offset_distance"/>
        <prop v="MM" k="offset_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="offset_unit_scale"/>
        <prop v="1" k="opacity"/>
      </effect>
      <effect type="innerGlow">
        <Option type="Map">
          <Option name="blend_mode" type="QString" value="0"/>
          <Option name="blur_level" type="QString" value="2.645"/>
          <Option name="blur_unit" type="QString" value="MM"/>
          <Option name="blur_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
          <Option name="color1" type="QString" value="69,116,40,255"/>
          <Option name="color2" type="QString" value="188,220,60,255"/>
          <Option name="color_type" type="QString" value="0"/>
          <Option name="direction" type="QString" value="ccw"/>
          <Option name="discrete" type="QString" value="0"/>
          <Option name="draw_mode" type="QString" value="2"/>
          <Option name="enabled" type="QString" value="0"/>
          <Option name="opacity" type="QString" value="0.5"/>
          <Option name="rampType" type="QString" value="gradient"/>
          <Option name="single_color" type="QString" value="255,255,255,255"/>
          <Option name="spec" type="QString" value="rgb"/>
          <Option name="spread" type="QString" value="2"/>
          <Option name="spread_unit" type="QString" value="MM"/>
          <Option name="spread_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
        </Option>
        <prop v="0" k="blend_mode"/>
        <prop v="2.645" k="blur_level"/>
        <prop v="MM" k="blur_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="blur_unit_scale"/>
        <prop v="69,116,40,255" k="color1"/>
        <prop v="188,220,60,255" k="color2"/>
        <prop v="0" k="color_type"/>
        <prop v="ccw" k="direction"/>
        <prop v="0" k="discrete"/>
        <prop v="2" k="draw_mode"/>
        <prop v="0" k="enabled"/>
        <prop v="0.5" k="opacity"/>
        <prop v="gradient" k="rampType"/>
        <prop v="255,255,255,255" k="single_color"/>
        <prop v="rgb" k="spec"/>
        <prop v="2" k="spread"/>
        <prop v="MM" k="spread_unit"/>
        <prop v="3x:0,0,0,0,0,0" k="spread_unit_scale"/>
      </effect>
    </effect>
  </renderer-v2>
  <labeling type="rule-based">
    <rules key="{2f71173c-e661-419f-adb6-81f4e57a6e61}">
      <rule scalemindenom="500" key="{380cf3a4-326d-4a4c-8c46-4eb18a039b4e}" scalemaxdenom="10000">
        <settings calloutType="simple">
          <text-style fontLetterSpacing="0" multilineHeight="1" isExpression="0" fontItalic="0" fontKerning="1" legendString="Aa" textOpacity="1" fontWeight="50" fontFamily="Arial" fontStrikeout="0" capitalization="0" fontSizeMapUnitScale="3x:0,0,0,0,0,0" previewBkgrdColor="255,255,255,255" fontWordSpacing="0" fieldName="filename" textOrientation="horizontal" useSubstitutions="0" textColor="50,50,50,255" fontSize="10" fontSizeUnit="Point" allowHtml="0" blendMode="0" fontUnderline="0" namedStyle="Regular">
            <families/>
            <text-buffer bufferNoFill="1" bufferBlendMode="0" bufferColor="250,250,250,255" bufferOpacity="1" bufferSize="1" bufferSizeUnits="MM" bufferJoinStyle="128" bufferDraw="0" bufferSizeMapUnitScale="3x:0,0,0,0,0,0"/>
            <text-mask maskSizeMapUnitScale="3x:0,0,0,0,0,0" maskedSymbolLayers="" maskJoinStyle="128" maskSize="0" maskSizeUnits="MM" maskOpacity="1" maskEnabled="0" maskType="0"/>
            <background shapeJoinStyle="64" shapeBorderColor="128,128,128,255" shapeOffsetMapUnitScale="3x:0,0,0,0,0,0" shapeSizeUnit="Point" shapeOpacity="1" shapeOffsetUnit="Point" shapeSizeMapUnitScale="3x:0,0,0,0,0,0" shapeRadiiX="0" shapeBorderWidth="0" shapeRadiiMapUnitScale="3x:0,0,0,0,0,0" shapeSizeY="0" shapeBlendMode="0" shapeOffsetX="0" shapeSizeType="0" shapeRadiiUnit="Point" shapeRotationType="0" shapeRotation="0" shapeDraw="0" shapeBorderWidthMapUnitScale="3x:0,0,0,0,0,0" shapeOffsetY="0" shapeSVGFile="" shapeSizeX="0" shapeFillColor="255,255,255,255" shapeType="0" shapeBorderWidthUnit="Point" shapeRadiiY="0">
              <symbol name="markerSymbol" force_rhr="0" clip_to_extent="1" type="marker" alpha="1">
                <data_defined_properties>
                  <Option type="Map">
                    <Option name="name" type="QString" value=""/>
                    <Option name="properties"/>
                    <Option name="type" type="QString" value="collection"/>
                  </Option>
                </data_defined_properties>
                <layer locked="0" class="SimpleMarker" enabled="1" pass="0">
                  <Option type="Map">
                    <Option name="angle" type="QString" value="0"/>
                    <Option name="cap_style" type="QString" value="square"/>
                    <Option name="color" type="QString" value="231,113,72,255"/>
                    <Option name="horizontal_anchor_point" type="QString" value="1"/>
                    <Option name="joinstyle" type="QString" value="bevel"/>
                    <Option name="name" type="QString" value="circle"/>
                    <Option name="offset" type="QString" value="0,0"/>
                    <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="offset_unit" type="QString" value="MM"/>
                    <Option name="outline_color" type="QString" value="35,35,35,255"/>
                    <Option name="outline_style" type="QString" value="solid"/>
                    <Option name="outline_width" type="QString" value="0"/>
                    <Option name="outline_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="outline_width_unit" type="QString" value="MM"/>
                    <Option name="scale_method" type="QString" value="diameter"/>
                    <Option name="size" type="QString" value="2"/>
                    <Option name="size_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="size_unit" type="QString" value="MM"/>
                    <Option name="vertical_anchor_point" type="QString" value="1"/>
                  </Option>
                  <prop v="0" k="angle"/>
                  <prop v="square" k="cap_style"/>
                  <prop v="231,113,72,255" k="color"/>
                  <prop v="1" k="horizontal_anchor_point"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="circle" k="name"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="35,35,35,255" k="outline_color"/>
                  <prop v="solid" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
                  <prop v="MM" k="outline_width_unit"/>
                  <prop v="diameter" k="scale_method"/>
                  <prop v="2" k="size"/>
                  <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
                  <prop v="MM" k="size_unit"/>
                  <prop v="1" k="vertical_anchor_point"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" type="QString" value=""/>
                      <Option name="properties"/>
                      <Option name="type" type="QString" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
              <symbol name="fillSymbol" force_rhr="0" clip_to_extent="1" type="fill" alpha="1">
                <data_defined_properties>
                  <Option type="Map">
                    <Option name="name" type="QString" value=""/>
                    <Option name="properties"/>
                    <Option name="type" type="QString" value="collection"/>
                  </Option>
                </data_defined_properties>
                <layer locked="0" class="SimpleFill" enabled="1" pass="0">
                  <Option type="Map">
                    <Option name="border_width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="color" type="QString" value="255,255,255,255"/>
                    <Option name="joinstyle" type="QString" value="bevel"/>
                    <Option name="offset" type="QString" value="0,0"/>
                    <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
                    <Option name="offset_unit" type="QString" value="MM"/>
                    <Option name="outline_color" type="QString" value="128,128,128,255"/>
                    <Option name="outline_style" type="QString" value="no"/>
                    <Option name="outline_width" type="QString" value="0"/>
                    <Option name="outline_width_unit" type="QString" value="Point"/>
                    <Option name="style" type="QString" value="solid"/>
                  </Option>
                  <prop v="3x:0,0,0,0,0,0" k="border_width_map_unit_scale"/>
                  <prop v="255,255,255,255" k="color"/>
                  <prop v="bevel" k="joinstyle"/>
                  <prop v="0,0" k="offset"/>
                  <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
                  <prop v="MM" k="offset_unit"/>
                  <prop v="128,128,128,255" k="outline_color"/>
                  <prop v="no" k="outline_style"/>
                  <prop v="0" k="outline_width"/>
                  <prop v="Point" k="outline_width_unit"/>
                  <prop v="solid" k="style"/>
                  <data_defined_properties>
                    <Option type="Map">
                      <Option name="name" type="QString" value=""/>
                      <Option name="properties"/>
                      <Option name="type" type="QString" value="collection"/>
                    </Option>
                  </data_defined_properties>
                </layer>
              </symbol>
            </background>
            <shadow shadowOffsetGlobal="1" shadowRadiusMapUnitScale="3x:0,0,0,0,0,0" shadowBlendMode="6" shadowDraw="0" shadowRadius="1.5" shadowOffsetUnit="MM" shadowUnder="0" shadowOffsetAngle="135" shadowColor="0,0,0,255" shadowOffsetMapUnitScale="3x:0,0,0,0,0,0" shadowRadiusUnit="MM" shadowRadiusAlphaOnly="0" shadowOpacity="0.69999999999999996" shadowScale="100" shadowOffsetDist="1"/>
            <dd_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </dd_properties>
            <substitutions/>
          </text-style>
          <text-format useMaxLineLengthForAutoWrap="1" leftDirectionSymbol="&lt;" multilineAlign="3" addDirectionSymbol="0" placeDirectionSymbol="0" plussign="0" formatNumbers="0" reverseDirectionSymbol="0" rightDirectionSymbol=">" autoWrapLength="0" wrapChar="" decimals="3"/>
          <placement labelOffsetMapUnitScale="3x:0,0,0,0,0,0" lineAnchorPercent="0.5" repeatDistanceUnits="MM" centroidWhole="0" distUnits="MM" polygonPlacementFlags="2" layerType="PolygonGeometry" geometryGeneratorEnabled="0" overrunDistanceUnit="MM" geometryGenerator="" maxCurvedCharAngleOut="-25" repeatDistanceMapUnitScale="3x:0,0,0,0,0,0" dist="0" rotationAngle="0" overrunDistanceMapUnitScale="3x:0,0,0,0,0,0" placement="0" lineAnchorClipping="0" priority="5" yOffset="0" offsetType="0" rotationUnit="AngleDegrees" maxCurvedCharAngleIn="25" preserveRotation="1" distMapUnitScale="3x:0,0,0,0,0,0" xOffset="0" quadOffset="4" geometryGeneratorType="PointGeometry" offsetUnits="MM" predefinedPositionOrder="TR,TL,BR,BL,R,L,TSR,BSR" centroidInside="0" placementFlags="10" repeatDistance="0" fitInPolygonOnly="0" overrunDistance="0" lineAnchorType="0"/>
          <rendering zIndex="0" scaleVisibility="0" fontMaxPixelSize="10000" fontMinPixelSize="3" labelPerPart="0" mergeLines="0" scaleMin="0" limitNumLabels="0" obstacleType="1" fontLimitPixelSize="0" displayAll="0" unplacedVisibility="0" upsidedownLabels="0" obstacleFactor="1" scaleMax="0" maxNumLabels="2000" obstacle="1" minFeatureSize="0" drawLabels="1"/>
          <dd_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </dd_properties>
          <callout type="simple">
            <Option type="Map">
              <Option name="anchorPoint" type="QString" value="pole_of_inaccessibility"/>
              <Option name="blendMode" type="int" value="0"/>
              <Option name="ddProperties" type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
              <Option name="drawToAllParts" type="bool" value="false"/>
              <Option name="enabled" type="QString" value="0"/>
              <Option name="labelAnchorPoint" type="QString" value="point_on_exterior"/>
              <Option name="lineSymbol" type="QString" value="&lt;symbol name=&quot;symbol&quot; force_rhr=&quot;0&quot; clip_to_extent=&quot;1&quot; type=&quot;line&quot; alpha=&quot;1&quot;>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;layer locked=&quot;0&quot; class=&quot;SimpleLine&quot; enabled=&quot;1&quot; pass=&quot;0&quot;>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;align_dash_pattern&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;capstyle&quot; type=&quot;QString&quot; value=&quot;square&quot;/>&lt;Option name=&quot;customdash&quot; type=&quot;QString&quot; value=&quot;5;2&quot;/>&lt;Option name=&quot;customdash_map_unit_scale&quot; type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option name=&quot;customdash_unit&quot; type=&quot;QString&quot; value=&quot;MM&quot;/>&lt;Option name=&quot;dash_pattern_offset&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;dash_pattern_offset_map_unit_scale&quot; type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option name=&quot;dash_pattern_offset_unit&quot; type=&quot;QString&quot; value=&quot;MM&quot;/>&lt;Option name=&quot;draw_inside_polygon&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;joinstyle&quot; type=&quot;QString&quot; value=&quot;bevel&quot;/>&lt;Option name=&quot;line_color&quot; type=&quot;QString&quot; value=&quot;60,60,60,255&quot;/>&lt;Option name=&quot;line_style&quot; type=&quot;QString&quot; value=&quot;solid&quot;/>&lt;Option name=&quot;line_width&quot; type=&quot;QString&quot; value=&quot;0.3&quot;/>&lt;Option name=&quot;line_width_unit&quot; type=&quot;QString&quot; value=&quot;MM&quot;/>&lt;Option name=&quot;offset&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;offset_map_unit_scale&quot; type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option name=&quot;offset_unit&quot; type=&quot;QString&quot; value=&quot;MM&quot;/>&lt;Option name=&quot;ring_filter&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;trim_distance_end&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;trim_distance_end_map_unit_scale&quot; type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option name=&quot;trim_distance_end_unit&quot; type=&quot;QString&quot; value=&quot;MM&quot;/>&lt;Option name=&quot;trim_distance_start&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;trim_distance_start_map_unit_scale&quot; type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;Option name=&quot;trim_distance_start_unit&quot; type=&quot;QString&quot; value=&quot;MM&quot;/>&lt;Option name=&quot;tweak_dash_pattern_on_corners&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;use_custom_dash&quot; type=&quot;QString&quot; value=&quot;0&quot;/>&lt;Option name=&quot;width_map_unit_scale&quot; type=&quot;QString&quot; value=&quot;3x:0,0,0,0,0,0&quot;/>&lt;/Option>&lt;prop v=&quot;0&quot; k=&quot;align_dash_pattern&quot;/>&lt;prop v=&quot;square&quot; k=&quot;capstyle&quot;/>&lt;prop v=&quot;5;2&quot; k=&quot;customdash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;customdash_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;customdash_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;dash_pattern_offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;dash_pattern_offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;dash_pattern_offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;draw_inside_polygon&quot;/>&lt;prop v=&quot;bevel&quot; k=&quot;joinstyle&quot;/>&lt;prop v=&quot;60,60,60,255&quot; k=&quot;line_color&quot;/>&lt;prop v=&quot;solid&quot; k=&quot;line_style&quot;/>&lt;prop v=&quot;0.3&quot; k=&quot;line_width&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;line_width_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;offset&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;offset_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;offset_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;ring_filter&quot;/>&lt;prop v=&quot;0&quot; k=&quot;trim_distance_end&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;trim_distance_end_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;trim_distance_end_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;trim_distance_start&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;trim_distance_start_map_unit_scale&quot;/>&lt;prop v=&quot;MM&quot; k=&quot;trim_distance_start_unit&quot;/>&lt;prop v=&quot;0&quot; k=&quot;tweak_dash_pattern_on_corners&quot;/>&lt;prop v=&quot;0&quot; k=&quot;use_custom_dash&quot;/>&lt;prop v=&quot;3x:0,0,0,0,0,0&quot; k=&quot;width_map_unit_scale&quot;/>&lt;data_defined_properties>&lt;Option type=&quot;Map&quot;>&lt;Option name=&quot;name&quot; type=&quot;QString&quot; value=&quot;&quot;/>&lt;Option name=&quot;properties&quot;/>&lt;Option name=&quot;type&quot; type=&quot;QString&quot; value=&quot;collection&quot;/>&lt;/Option>&lt;/data_defined_properties>&lt;/layer>&lt;/symbol>"/>
              <Option name="minLength" type="double" value="0"/>
              <Option name="minLengthMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="minLengthUnit" type="QString" value="MM"/>
              <Option name="offsetFromAnchor" type="double" value="0"/>
              <Option name="offsetFromAnchorMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromAnchorUnit" type="QString" value="MM"/>
              <Option name="offsetFromLabel" type="double" value="0"/>
              <Option name="offsetFromLabelMapUnitScale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offsetFromLabelUnit" type="QString" value="MM"/>
            </Option>
          </callout>
        </settings>
      </rule>
    </rules>
  </labeling>
  <customproperties>
    <Option type="Map">
      <Option name="dualview/previewExpressions" type="StringList">
        <Option type="QString" value="NAME"/>
      </Option>
      <Option name="embeddedWidgets/count" type="QString" value="0"/>
      <Option name="variableNames"/>
      <Option name="variableValues"/>
    </Option>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer diagramType="Histogram" attributeLegend="1">
    <DiagramCategory spacing="5" scaleDependency="Area" barWidth="5" spacingUnitScale="3x:0,0,0,0,0,0" minScaleDenominator="0" lineSizeType="MM" penWidth="0" penAlpha="255" maxScaleDenominator="0" lineSizeScale="3x:0,0,0,0,0,0" minimumSize="0" width="15" enabled="0" sizeScale="3x:0,0,0,0,0,0" opacity="1" backgroundColor="#ffffff" scaleBasedVisibility="0" rotationOffset="270" diagramOrientation="Up" spacingUnit="MM" direction="0" height="15" penColor="#000000" sizeType="MM" showAxis="1" backgroundAlpha="255" labelPlacementMethod="XHeight">
      <fontProperties description="MS Shell Dlg 2,9.6,-1,5,50,0,0,0,0,0" style=""/>
      <attribute color="#000000" label="" field=""/>
      <axisSymbol>
        <symbol name="" force_rhr="0" clip_to_extent="1" type="line" alpha="1">
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" type="QString" value=""/>
              <Option name="properties"/>
              <Option name="type" type="QString" value="collection"/>
            </Option>
          </data_defined_properties>
          <layer locked="0" class="SimpleLine" enabled="1" pass="0">
            <Option type="Map">
              <Option name="align_dash_pattern" type="QString" value="0"/>
              <Option name="capstyle" type="QString" value="square"/>
              <Option name="customdash" type="QString" value="5;2"/>
              <Option name="customdash_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="customdash_unit" type="QString" value="MM"/>
              <Option name="dash_pattern_offset" type="QString" value="0"/>
              <Option name="dash_pattern_offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="dash_pattern_offset_unit" type="QString" value="MM"/>
              <Option name="draw_inside_polygon" type="QString" value="0"/>
              <Option name="joinstyle" type="QString" value="bevel"/>
              <Option name="line_color" type="QString" value="35,35,35,255"/>
              <Option name="line_style" type="QString" value="solid"/>
              <Option name="line_width" type="QString" value="0.26"/>
              <Option name="line_width_unit" type="QString" value="MM"/>
              <Option name="offset" type="QString" value="0"/>
              <Option name="offset_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="offset_unit" type="QString" value="MM"/>
              <Option name="ring_filter" type="QString" value="0"/>
              <Option name="trim_distance_end" type="QString" value="0"/>
              <Option name="trim_distance_end_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="trim_distance_end_unit" type="QString" value="MM"/>
              <Option name="trim_distance_start" type="QString" value="0"/>
              <Option name="trim_distance_start_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
              <Option name="trim_distance_start_unit" type="QString" value="MM"/>
              <Option name="tweak_dash_pattern_on_corners" type="QString" value="0"/>
              <Option name="use_custom_dash" type="QString" value="0"/>
              <Option name="width_map_unit_scale" type="QString" value="3x:0,0,0,0,0,0"/>
            </Option>
            <prop v="0" k="align_dash_pattern"/>
            <prop v="square" k="capstyle"/>
            <prop v="5;2" k="customdash"/>
            <prop v="3x:0,0,0,0,0,0" k="customdash_map_unit_scale"/>
            <prop v="MM" k="customdash_unit"/>
            <prop v="0" k="dash_pattern_offset"/>
            <prop v="3x:0,0,0,0,0,0" k="dash_pattern_offset_map_unit_scale"/>
            <prop v="MM" k="dash_pattern_offset_unit"/>
            <prop v="0" k="draw_inside_polygon"/>
            <prop v="bevel" k="joinstyle"/>
            <prop v="35,35,35,255" k="line_color"/>
            <prop v="solid" k="line_style"/>
            <prop v="0.26" k="line_width"/>
            <prop v="MM" k="line_width_unit"/>
            <prop v="0" k="offset"/>
            <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
            <prop v="MM" k="offset_unit"/>
            <prop v="0" k="ring_filter"/>
            <prop v="0" k="trim_distance_end"/>
            <prop v="3x:0,0,0,0,0,0" k="trim_distance_end_map_unit_scale"/>
            <prop v="MM" k="trim_distance_end_unit"/>
            <prop v="0" k="trim_distance_start"/>
            <prop v="3x:0,0,0,0,0,0" k="trim_distance_start_map_unit_scale"/>
            <prop v="MM" k="trim_distance_start_unit"/>
            <prop v="0" k="tweak_dash_pattern_on_corners"/>
            <prop v="0" k="use_custom_dash"/>
            <prop v="3x:0,0,0,0,0,0" k="width_map_unit_scale"/>
            <data_defined_properties>
              <Option type="Map">
                <Option name="name" type="QString" value=""/>
                <Option name="properties"/>
                <Option name="type" type="QString" value="collection"/>
              </Option>
            </data_defined_properties>
          </layer>
        </symbol>
      </axisSymbol>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings zIndex="0" priority="0" showAll="1" linePlacementFlags="18" placement="1" dist="0" obstacle="0">
    <properties>
      <Option type="Map">
        <Option name="name" type="QString" value=""/>
        <Option name="properties"/>
        <Option name="type" type="QString" value="collection"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions removeDuplicateNodes="0" geometryPrecision="0">
    <activeChecks/>
    <checkConfiguration type="Map">
      <Option name="QgsGeometryGapCheck" type="Map">
        <Option name="allowedGapsBuffer" type="double" value="0"/>
        <Option name="allowedGapsEnabled" type="bool" value="false"/>
        <Option name="allowedGapsLayer" type="QString" value=""/>
      </Option>
    </checkConfiguration>
  </geometryOptions>
  <legend type="default-vector" showLabelLegend="0"/>
  <referencedLayers/>
  <fieldConfiguration>
    <field name="fid" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="filename" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="file_source_id" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="encoding" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="las_version" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="point_data_format" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="scale_factor" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="header_min_x" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="header_max_x" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="header_min_y" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="header_max_y" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="header_min_z" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="header_max_z" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="point_coordinates_match_header" configurationFlags="None">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="intensity_min" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="intensity_max" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="return_number_min" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="return_number_max" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="scan_angle_min" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="scan_angle_max" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="point_source_id_min" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="point_source_id_max" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gps_time_min" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gps_time_max" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="is_tiling_correct" configurationFlags="None">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="is_file_name_correct_format" configurationFlags="None">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="is_file_name_correct_tile" configurationFlags="None">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="is_projection_correct" configurationFlags="None">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="is_in_supplied_tile_index" configurationFlags="None">
      <editWidget type="CheckBox">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="classifications" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="unclassified" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="ground" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="low_veg" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="med_veg" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="high_veg" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="building" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="low_noise" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="water" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="high_noise" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="other_classes" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="overlap_flag" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="withheld_flag" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="point_density" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pulse_density_first" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pulse_density_last" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="warnings" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="errors" configurationFlags="None">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="" index="0" field="fid"/>
    <alias name="" index="1" field="filename"/>
    <alias name="" index="2" field="file_source_id"/>
    <alias name="" index="3" field="encoding"/>
    <alias name="" index="4" field="las_version"/>
    <alias name="" index="5" field="point_data_format"/>
    <alias name="" index="6" field="scale_factor"/>
    <alias name="" index="7" field="header_min_x"/>
    <alias name="" index="8" field="header_max_x"/>
    <alias name="" index="9" field="header_min_y"/>
    <alias name="" index="10" field="header_max_y"/>
    <alias name="" index="11" field="header_min_z"/>
    <alias name="" index="12" field="header_max_z"/>
    <alias name="" index="13" field="point_coordinates_match_header"/>
    <alias name="" index="14" field="intensity_min"/>
    <alias name="" index="15" field="intensity_max"/>
    <alias name="" index="16" field="return_number_min"/>
    <alias name="" index="17" field="return_number_max"/>
    <alias name="" index="18" field="scan_angle_min"/>
    <alias name="" index="19" field="scan_angle_max"/>
    <alias name="" index="20" field="point_source_id_min"/>
    <alias name="" index="21" field="point_source_id_max"/>
    <alias name="" index="22" field="gps_time_min"/>
    <alias name="" index="23" field="gps_time_max"/>
    <alias name="" index="24" field="is_tiling_correct"/>
    <alias name="" index="25" field="is_file_name_correct_format"/>
    <alias name="" index="26" field="is_file_name_correct_tile"/>
    <alias name="" index="27" field="is_projection_correct"/>
    <alias name="" index="28" field="is_in_supplied_tile_index"/>
    <alias name="" index="29" field="classifications"/>
    <alias name="" index="30" field="unclassified"/>
    <alias name="" index="31" field="ground"/>
    <alias name="" index="32" field="low_veg"/>
    <alias name="" index="33" field="med_veg"/>
    <alias name="" index="34" field="high_veg"/>
    <alias name="" index="35" field="building"/>
    <alias name="" index="36" field="low_noise"/>
    <alias name="" index="37" field="water"/>
    <alias name="" index="38" field="high_noise"/>
    <alias name="" index="39" field="other_classes"/>
    <alias name="" index="40" field="overlap_flag"/>
    <alias name="" index="41" field="withheld_flag"/>
    <alias name="" index="42" field="point_density"/>
    <alias name="" index="43" field="pulse_density_first"/>
    <alias name="" index="44" field="pulse_density_last"/>
    <alias name="" index="45" field="warnings"/>
    <alias name="" index="46" field="errors"/>
  </aliases>
  <defaults>
    <default applyOnUpdate="0" expression="" field="fid"/>
    <default applyOnUpdate="0" expression="" field="filename"/>
    <default applyOnUpdate="0" expression="" field="file_source_id"/>
    <default applyOnUpdate="0" expression="" field="encoding"/>
    <default applyOnUpdate="0" expression="" field="las_version"/>
    <default applyOnUpdate="0" expression="" field="point_data_format"/>
    <default applyOnUpdate="0" expression="" field="scale_factor"/>
    <default applyOnUpdate="0" expression="" field="header_min_x"/>
    <default applyOnUpdate="0" expression="" field="header_max_x"/>
    <default applyOnUpdate="0" expression="" field="header_min_y"/>
    <default applyOnUpdate="0" expression="" field="header_max_y"/>
    <default applyOnUpdate="0" expression="" field="header_min_z"/>
    <default applyOnUpdate="0" expression="" field="header_max_z"/>
    <default applyOnUpdate="0" expression="" field="point_coordinates_match_header"/>
    <default applyOnUpdate="0" expression="" field="intensity_min"/>
    <default applyOnUpdate="0" expression="" field="intensity_max"/>
    <default applyOnUpdate="0" expression="" field="return_number_min"/>
    <default applyOnUpdate="0" expression="" field="return_number_max"/>
    <default applyOnUpdate="0" expression="" field="scan_angle_min"/>
    <default applyOnUpdate="0" expression="" field="scan_angle_max"/>
    <default applyOnUpdate="0" expression="" field="point_source_id_min"/>
    <default applyOnUpdate="0" expression="" field="point_source_id_max"/>
    <default applyOnUpdate="0" expression="" field="gps_time_min"/>
    <default applyOnUpdate="0" expression="" field="gps_time_max"/>
    <default applyOnUpdate="0" expression="" field="is_tiling_correct"/>
    <default applyOnUpdate="0" expression="" field="is_file_name_correct_format"/>
    <default applyOnUpdate="0" expression="" field="is_file_name_correct_tile"/>
    <default applyOnUpdate="0" expression="" field="is_projection_correct"/>
    <default applyOnUpdate="0" expression="" field="is_in_supplied_tile_index"/>
    <default applyOnUpdate="0" expression="" field="classifications"/>
    <default applyOnUpdate="0" expression="" field="unclassified"/>
    <default applyOnUpdate="0" expression="" field="ground"/>
    <default applyOnUpdate="0" expression="" field="low_veg"/>
    <default applyOnUpdate="0" expression="" field="med_veg"/>
    <default applyOnUpdate="0" expression="" field="high_veg"/>
    <default applyOnUpdate="0" expression="" field="building"/>
    <default applyOnUpdate="0" expression="" field="low_noise"/>
    <default applyOnUpdate="0" expression="" field="water"/>
    <default applyOnUpdate="0" expression="" field="high_noise"/>
    <default applyOnUpdate="0" expression="" field="other_classes"/>
    <default applyOnUpdate="0" expression="" field="overlap_flag"/>
    <default applyOnUpdate="0" expression="" field="withheld_flag"/>
    <default applyOnUpdate="0" expression="" field="point_density"/>
    <default applyOnUpdate="0" expression="" field="pulse_density_first"/>
    <default applyOnUpdate="0" expression="" field="pulse_density_last"/>
    <default applyOnUpdate="0" expression="" field="warnings"/>
    <default applyOnUpdate="0" expression="" field="errors"/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" unique_strength="1" notnull_strength="1" field="fid" constraints="3"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="filename" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="file_source_id" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="encoding" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="las_version" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="point_data_format" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="scale_factor" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="header_min_x" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="header_max_x" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="header_min_y" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="header_max_y" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="header_min_z" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="header_max_z" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="point_coordinates_match_header" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="intensity_min" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="intensity_max" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="return_number_min" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="return_number_max" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="scan_angle_min" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="scan_angle_max" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="point_source_id_min" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="point_source_id_max" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="gps_time_min" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="gps_time_max" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="is_tiling_correct" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="is_file_name_correct_format" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="is_file_name_correct_tile" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="is_projection_correct" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="is_in_supplied_tile_index" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="classifications" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="unclassified" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="ground" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="low_veg" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="med_veg" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="high_veg" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="building" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="low_noise" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="water" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="high_noise" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="other_classes" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="overlap_flag" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="withheld_flag" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="point_density" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="pulse_density_first" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="pulse_density_last" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="warnings" constraints="0"/>
    <constraint exp_strength="0" unique_strength="0" notnull_strength="0" field="errors" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" field="fid" desc=""/>
    <constraint exp="" field="filename" desc=""/>
    <constraint exp="" field="file_source_id" desc=""/>
    <constraint exp="" field="encoding" desc=""/>
    <constraint exp="" field="las_version" desc=""/>
    <constraint exp="" field="point_data_format" desc=""/>
    <constraint exp="" field="scale_factor" desc=""/>
    <constraint exp="" field="header_min_x" desc=""/>
    <constraint exp="" field="header_max_x" desc=""/>
    <constraint exp="" field="header_min_y" desc=""/>
    <constraint exp="" field="header_max_y" desc=""/>
    <constraint exp="" field="header_min_z" desc=""/>
    <constraint exp="" field="header_max_z" desc=""/>
    <constraint exp="" field="point_coordinates_match_header" desc=""/>
    <constraint exp="" field="intensity_min" desc=""/>
    <constraint exp="" field="intensity_max" desc=""/>
    <constraint exp="" field="return_number_min" desc=""/>
    <constraint exp="" field="return_number_max" desc=""/>
    <constraint exp="" field="scan_angle_min" desc=""/>
    <constraint exp="" field="scan_angle_max" desc=""/>
    <constraint exp="" field="point_source_id_min" desc=""/>
    <constraint exp="" field="point_source_id_max" desc=""/>
    <constraint exp="" field="gps_time_min" desc=""/>
    <constraint exp="" field="gps_time_max" desc=""/>
    <constraint exp="" field="is_tiling_correct" desc=""/>
    <constraint exp="" field="is_file_name_correct_format" desc=""/>
    <constraint exp="" field="is_file_name_correct_tile" desc=""/>
    <constraint exp="" field="is_projection_correct" desc=""/>
    <constraint exp="" field="is_in_supplied_tile_index" desc=""/>
    <constraint exp="" field="classifications" desc=""/>
    <constraint exp="" field="unclassified" desc=""/>
    <constraint exp="" field="ground" desc=""/>
    <constraint exp="" field="low_veg" desc=""/>
    <constraint exp="" field="med_veg" desc=""/>
    <constraint exp="" field="high_veg" desc=""/>
    <constraint exp="" field="building" desc=""/>
    <constraint exp="" field="low_noise" desc=""/>
    <constraint exp="" field="water" desc=""/>
    <constraint exp="" field="high_noise" desc=""/>
    <constraint exp="" field="other_classes" desc=""/>
    <constraint exp="" field="overlap_flag" desc=""/>
    <constraint exp="" field="withheld_flag" desc=""/>
    <constraint exp="" field="point_density" desc=""/>
    <constraint exp="" field="pulse_density_first" desc=""/>
    <constraint exp="" field="pulse_density_last" desc=""/>
    <constraint exp="" field="warnings" desc=""/>
    <constraint exp="" field="errors" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column name="fid" hidden="0" type="field" width="-1"/>
      <column name="filename" hidden="0" type="field" width="-1"/>
      <column name="file_source_id" hidden="0" type="field" width="-1"/>
      <column name="encoding" hidden="0" type="field" width="-1"/>
      <column name="las_version" hidden="0" type="field" width="-1"/>
      <column name="point_data_format" hidden="0" type="field" width="-1"/>
      <column name="scale_factor" hidden="0" type="field" width="-1"/>
      <column name="header_min_x" hidden="0" type="field" width="-1"/>
      <column name="header_max_x" hidden="0" type="field" width="-1"/>
      <column name="header_min_y" hidden="0" type="field" width="-1"/>
      <column name="header_max_y" hidden="0" type="field" width="-1"/>
      <column name="header_min_z" hidden="0" type="field" width="-1"/>
      <column name="header_max_z" hidden="0" type="field" width="-1"/>
      <column name="point_coordinates_match_header" hidden="0" type="field" width="-1"/>
      <column name="intensity_min" hidden="0" type="field" width="-1"/>
      <column name="intensity_max" hidden="0" type="field" width="-1"/>
      <column name="return_number_min" hidden="0" type="field" width="-1"/>
      <column name="return_number_max" hidden="0" type="field" width="-1"/>
      <column name="scan_angle_min" hidden="0" type="field" width="-1"/>
      <column name="scan_angle_max" hidden="0" type="field" width="-1"/>
      <column name="point_source_id_min" hidden="0" type="field" width="-1"/>
      <column name="point_source_id_max" hidden="0" type="field" width="-1"/>
      <column name="is_in_supplied_tile_index" hidden="0" type="field" width="-1"/>
      <column name="classifications" hidden="0" type="field" width="-1"/>
      <column name="unclassified" hidden="0" type="field" width="-1"/>
      <column name="ground" hidden="0" type="field" width="-1"/>
      <column name="low_veg" hidden="0" type="field" width="-1"/>
      <column name="med_veg" hidden="0" type="field" width="-1"/>
      <column name="high_veg" hidden="0" type="field" width="-1"/>
      <column name="building" hidden="0" type="field" width="-1"/>
      <column name="low_noise" hidden="0" type="field" width="-1"/>
      <column name="water" hidden="0" type="field" width="-1"/>
      <column name="high_noise" hidden="0" type="field" width="-1"/>
      <column name="other_classes" hidden="0" type="field" width="-1"/>
      <column name="overlap_flag" hidden="0" type="field" width="-1"/>
      <column name="withheld_flag" hidden="0" type="field" width="-1"/>
      <column name="point_density" hidden="0" type="field" width="-1"/>
      <column name="pulse_density_first" hidden="0" type="field" width="-1"/>
      <column name="pulse_density_last" hidden="0" type="field" width="-1"/>
      <column name="warnings" hidden="0" type="field" width="-1"/>
      <column name="errors" hidden="0" type="field" width="-1"/>
      <column name="gps_time_min" hidden="0" type="field" width="-1"/>
      <column name="gps_time_max" hidden="0" type="field" width="-1"/>
      <column name="is_tiling_correct" hidden="0" type="field" width="-1"/>
      <column name="is_file_name_correct_format" hidden="0" type="field" width="-1"/>
      <column name="is_file_name_correct_tile" hidden="0" type="field" width="-1"/>
      <column name="is_projection_correct" hidden="0" type="field" width="-1"/>
      <column hidden="1" type="actions" width="-1"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="Class" editable="1"/>
    <field name="NAME" editable="1"/>
    <field name="building" editable="1"/>
    <field name="classifications" editable="1"/>
    <field name="created" editable="1"/>
    <field name="encoding" editable="1"/>
    <field name="errors" editable="1"/>
    <field name="fid" editable="1"/>
    <field name="file_source_id" editable="1"/>
    <field name="filename" editable="1"/>
    <field name="gps_time_max" editable="1"/>
    <field name="gps_time_min" editable="1"/>
    <field name="ground" editable="1"/>
    <field name="header_max_x" editable="1"/>
    <field name="header_max_y" editable="1"/>
    <field name="header_max_z" editable="1"/>
    <field name="header_min_x" editable="1"/>
    <field name="header_min_y" editable="1"/>
    <field name="header_min_z" editable="1"/>
    <field name="high_noise" editable="1"/>
    <field name="high_veg" editable="1"/>
    <field name="intensity_max" editable="1"/>
    <field name="intensity_min" editable="1"/>
    <field name="is_file_name_correct_format" editable="1"/>
    <field name="is_file_name_correct_tile" editable="1"/>
    <field name="is_in_supplied_tile_index" editable="1"/>
    <field name="is_projection_correct" editable="1"/>
    <field name="is_tiling_correct" editable="1"/>
    <field name="las_version" editable="1"/>
    <field name="low_noise" editable="1"/>
    <field name="low_veg" editable="1"/>
    <field name="med_veg" editable="1"/>
    <field name="modified" editable="1"/>
    <field name="other_classes" editable="1"/>
    <field name="overlap_flag" editable="1"/>
    <field name="point_coordinates_match_header" editable="1"/>
    <field name="point_data_format" editable="1"/>
    <field name="point_density" editable="1"/>
    <field name="point_source_id_max" editable="1"/>
    <field name="point_source_id_min" editable="1"/>
    <field name="pulse_density_first" editable="1"/>
    <field name="pulse_density_last" editable="1"/>
    <field name="return_number_max" editable="1"/>
    <field name="return_number_min" editable="1"/>
    <field name="scale_factor" editable="1"/>
    <field name="scan_angle_max" editable="1"/>
    <field name="scan_angle_min" editable="1"/>
    <field name="srs" editable="1"/>
    <field name="unclassified" editable="1"/>
    <field name="warnings" editable="1"/>
    <field name="water" editable="1"/>
    <field name="withheld_flag" editable="1"/>
    <field name="within_1k_tile" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="Class" labelOnTop="0"/>
    <field name="NAME" labelOnTop="0"/>
    <field name="building" labelOnTop="0"/>
    <field name="classifications" labelOnTop="0"/>
    <field name="created" labelOnTop="0"/>
    <field name="encoding" labelOnTop="0"/>
    <field name="errors" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="file_source_id" labelOnTop="0"/>
    <field name="filename" labelOnTop="0"/>
    <field name="gps_time_max" labelOnTop="0"/>
    <field name="gps_time_min" labelOnTop="0"/>
    <field name="ground" labelOnTop="0"/>
    <field name="header_max_x" labelOnTop="0"/>
    <field name="header_max_y" labelOnTop="0"/>
    <field name="header_max_z" labelOnTop="0"/>
    <field name="header_min_x" labelOnTop="0"/>
    <field name="header_min_y" labelOnTop="0"/>
    <field name="header_min_z" labelOnTop="0"/>
    <field name="high_noise" labelOnTop="0"/>
    <field name="high_veg" labelOnTop="0"/>
    <field name="intensity_max" labelOnTop="0"/>
    <field name="intensity_min" labelOnTop="0"/>
    <field name="is_file_name_correct_format" labelOnTop="0"/>
    <field name="is_file_name_correct_tile" labelOnTop="0"/>
    <field name="is_in_supplied_tile_index" labelOnTop="0"/>
    <field name="is_projection_correct" labelOnTop="0"/>
    <field name="is_tiling_correct" labelOnTop="0"/>
    <field name="las_version" labelOnTop="0"/>
    <field name="low_noise" labelOnTop="0"/>
    <field name="low_veg" labelOnTop="0"/>
    <field name="med_veg" labelOnTop="0"/>
    <field name="modified" labelOnTop="0"/>
    <field name="other_classes" labelOnTop="0"/>
    <field name="overlap_flag" labelOnTop="0"/>
    <field name="point_coordinates_match_header" labelOnTop="0"/>
    <field name="point_data_format" labelOnTop="0"/>
    <field name="point_density" labelOnTop="0"/>
    <field name="point_source_id_max" labelOnTop="0"/>
    <field name="point_source_id_min" labelOnTop="0"/>
    <field name="pulse_density_first" labelOnTop="0"/>
    <field name="pulse_density_last" labelOnTop="0"/>
    <field name="return_number_max" labelOnTop="0"/>
    <field name="return_number_min" labelOnTop="0"/>
    <field name="scale_factor" labelOnTop="0"/>
    <field name="scan_angle_max" labelOnTop="0"/>
    <field name="scan_angle_min" labelOnTop="0"/>
    <field name="srs" labelOnTop="0"/>
    <field name="unclassified" labelOnTop="0"/>
    <field name="warnings" labelOnTop="0"/>
    <field name="water" labelOnTop="0"/>
    <field name="withheld_flag" labelOnTop="0"/>
    <field name="within_1k_tile" labelOnTop="0"/>
  </labelOnTop>
  <reuseLastValue>
    <field name="building" reuseLastValue="0"/>
    <field name="classifications" reuseLastValue="0"/>
    <field name="encoding" reuseLastValue="0"/>
    <field name="errors" reuseLastValue="0"/>
    <field name="fid" reuseLastValue="0"/>
    <field name="file_source_id" reuseLastValue="0"/>
    <field name="filename" reuseLastValue="0"/>
    <field name="gps_time_max" reuseLastValue="0"/>
    <field name="gps_time_min" reuseLastValue="0"/>
    <field name="ground" reuseLastValue="0"/>
    <field name="header_max_x" reuseLastValue="0"/>
    <field name="header_max_y" reuseLastValue="0"/>
    <field name="header_max_z" reuseLastValue="0"/>
    <field name="header_min_x" reuseLastValue="0"/>
    <field name="header_min_y" reuseLastValue="0"/>
    <field name="header_min_z" reuseLastValue="0"/>
    <field name="high_noise" reuseLastValue="0"/>
    <field name="high_veg" reuseLastValue="0"/>
    <field name="intensity_max" reuseLastValue="0"/>
    <field name="intensity_min" reuseLastValue="0"/>
    <field name="is_file_name_correct_format" reuseLastValue="0"/>
    <field name="is_file_name_correct_tile" reuseLastValue="0"/>
    <field name="is_in_supplied_tile_index" reuseLastValue="0"/>
    <field name="is_projection_correct" reuseLastValue="0"/>
    <field name="is_tiling_correct" reuseLastValue="0"/>
    <field name="las_version" reuseLastValue="0"/>
    <field name="low_noise" reuseLastValue="0"/>
    <field name="low_veg" reuseLastValue="0"/>
    <field name="med_veg" reuseLastValue="0"/>
    <field name="other_classes" reuseLastValue="0"/>
    <field name="overlap_flag" reuseLastValue="0"/>
    <field name="point_coordinates_match_header" reuseLastValue="0"/>
    <field name="point_data_format" reuseLastValue="0"/>
    <field name="point_density" reuseLastValue="0"/>
    <field name="point_source_id_max" reuseLastValue="0"/>
    <field name="point_source_id_min" reuseLastValue="0"/>
    <field name="pulse_density_first" reuseLastValue="0"/>
    <field name="pulse_density_last" reuseLastValue="0"/>
    <field name="return_number_max" reuseLastValue="0"/>
    <field name="return_number_min" reuseLastValue="0"/>
    <field name="scale_factor" reuseLastValue="0"/>
    <field name="scan_angle_max" reuseLastValue="0"/>
    <field name="scan_angle_min" reuseLastValue="0"/>
    <field name="unclassified" reuseLastValue="0"/>
    <field name="warnings" reuseLastValue="0"/>
    <field name="water" reuseLastValue="0"/>
    <field name="withheld_flag" reuseLastValue="0"/>
    <field name="within_1k_tile" reuseLastValue="0"/>
  </reuseLastValue>
  <dataDefinedFieldProperties/>
  <widgets/>
  <previewExpression>NAME</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
