<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" version="3.24.0-Tisler" styleCategories="AllStyleCategories" hasScaleBasedVisibilityFlag="0" minScale="1e+08">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
    <Private>0</Private>
  </flags>
  <temporal fetchMode="0" mode="0" enabled="0">
    <fixedRange>
      <start></start>
      <end></end>
    </fixedRange>
  </temporal>
  <customproperties>
    <Option type="Map">
      <Option name="WMSBackgroundLayer" value="false" type="bool"/>
      <Option name="WMSPublishDataSourceUrl" value="false" type="bool"/>
      <Option name="embeddedWidgets/count" value="0" type="int"/>
      <Option name="identify/format" value="Value" type="QString"/>
    </Option>
  </customproperties>
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option name="name" value="" type="QString"/>
      <Option name="properties"/>
      <Option name="type" value="collection" type="QString"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling maxOversampling="2" zoomedOutResamplingMethod="nearestNeighbour" zoomedInResamplingMethod="nearestNeighbour" enabled="false"/>
    </provider>
    <rasterrenderer classificationMax="17" classificationMin="1" alphaBand="-1" band="1" opacity="1" type="singlebandpseudocolor" nodataColor="">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>MinMax</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="DISCRETE" labelPrecision="0" classificationMode="1" clip="0" maximumValue="17" minimumValue="1">
          <colorramp name="[source]" type="gradient">
            <Option type="Map">
              <Option name="color1" value="253,231,37,255" type="QString"/>
              <Option name="color2" value="68,1,84,255" type="QString"/>
              <Option name="direction" value="cw" type="QString"/>
              <Option name="discrete" value="0" type="QString"/>
              <Option name="rampType" value="gradient" type="QString"/>
              <Option name="spec" value="rgb" type="QString"/>
              <Option name="stops" value="0.019608;241,229,29,255;rgb;cw:0.039216;229,228,25,255;rgb;cw:0.058824;216,226,25,255;rgb;cw:0.078431;202,225,31,255;rgb;cw:0.098039;189,223,38,255;rgb;cw:0.117647;176,221,47,255;rgb;cw:0.137255;162,218,55,255;rgb;cw:0.156863;149,216,64,255;rgb;cw:0.176471;137,213,72,255;rgb;cw:0.196078;124,210,80,255;rgb;cw:0.215686;112,207,87,255;rgb;cw:0.235294;101,203,94,255;rgb;cw:0.254902;90,200,100,255;rgb;cw:0.27451;80,196,106,255;rgb;cw:0.294118;70,192,111,255;rgb;cw:0.313725;61,188,116,255;rgb;cw:0.333333;53,183,121,255;rgb;cw:0.352941;46,179,124,255;rgb;cw:0.372549;40,174,128,255;rgb;cw:0.392157;36,170,131,255;rgb;cw:0.411765;33,165,133,255;rgb;cw:0.431373;31,161,136,255;rgb;cw:0.45098;30,156,137,255;rgb;cw:0.470588;31,151,139,255;rgb;cw:0.490196;32,146,140,255;rgb;cw:0.509804;33,142,141,255;rgb;cw:0.529412;35,137,142,255;rgb;cw:0.54902;37,132,142,255;rgb;cw:0.568627;39,128,142,255;rgb;cw:0.588235;41,123,142,255;rgb;cw:0.607843;42,118,142,255;rgb;cw:0.627451;44,113,142,255;rgb;cw:0.647059;46,109,142,255;rgb;cw:0.666667;49,104,142,255;rgb;cw:0.686275;51,99,141,255;rgb;cw:0.705882;53,94,141,255;rgb;cw:0.72549;56,89,140,255;rgb;cw:0.745098;58,83,139,255;rgb;cw:0.764706;61,78,138,255;rgb;cw:0.784314;63,72,137,255;rgb;cw:0.803922;65,66,135,255;rgb;cw:0.823529;67,61,132,255;rgb;cw:0.843137;69,55,129,255;rgb;cw:0.862745;70,48,126,255;rgb;cw:0.882353;71,42,122,255;rgb;cw:0.901961;72,36,117,255;rgb;cw:0.921569;72,29,111,255;rgb;cw:0.941176;72,23,105,255;rgb;cw:0.960784;71,16,99,255;rgb;cw:0.980392;70,8,92,255;rgb;cw" type="QString"/>
            </Option>
            <prop v="253,231,37,255" k="color1"/>
            <prop v="68,1,84,255" k="color2"/>
            <prop v="cw" k="direction"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
            <prop v="rgb" k="spec"/>
            <prop v="0.019608;241,229,29,255;rgb;cw:0.039216;229,228,25,255;rgb;cw:0.058824;216,226,25,255;rgb;cw:0.078431;202,225,31,255;rgb;cw:0.098039;189,223,38,255;rgb;cw:0.117647;176,221,47,255;rgb;cw:0.137255;162,218,55,255;rgb;cw:0.156863;149,216,64,255;rgb;cw:0.176471;137,213,72,255;rgb;cw:0.196078;124,210,80,255;rgb;cw:0.215686;112,207,87,255;rgb;cw:0.235294;101,203,94,255;rgb;cw:0.254902;90,200,100,255;rgb;cw:0.27451;80,196,106,255;rgb;cw:0.294118;70,192,111,255;rgb;cw:0.313725;61,188,116,255;rgb;cw:0.333333;53,183,121,255;rgb;cw:0.352941;46,179,124,255;rgb;cw:0.372549;40,174,128,255;rgb;cw:0.392157;36,170,131,255;rgb;cw:0.411765;33,165,133,255;rgb;cw:0.431373;31,161,136,255;rgb;cw:0.45098;30,156,137,255;rgb;cw:0.470588;31,151,139,255;rgb;cw:0.490196;32,146,140,255;rgb;cw:0.509804;33,142,141,255;rgb;cw:0.529412;35,137,142,255;rgb;cw:0.54902;37,132,142,255;rgb;cw:0.568627;39,128,142,255;rgb;cw:0.588235;41,123,142,255;rgb;cw:0.607843;42,118,142,255;rgb;cw:0.627451;44,113,142,255;rgb;cw:0.647059;46,109,142,255;rgb;cw:0.666667;49,104,142,255;rgb;cw:0.686275;51,99,141,255;rgb;cw:0.705882;53,94,141,255;rgb;cw:0.72549;56,89,140,255;rgb;cw:0.745098;58,83,139,255;rgb;cw:0.764706;61,78,138,255;rgb;cw:0.784314;63,72,137,255;rgb;cw:0.803922;65,66,135,255;rgb;cw:0.823529;67,61,132,255;rgb;cw:0.843137;69,55,129,255;rgb;cw:0.862745;70,48,126,255;rgb;cw:0.882353;71,42,122,255;rgb;cw:0.901961;72,36,117,255;rgb;cw:0.921569;72,29,111,255;rgb;cw:0.941176;72,23,105,255;rgb;cw:0.960784;71,16,99,255;rgb;cw:0.980392;70,8,92,255;rgb;cw" k="stops"/>
          </colorramp>
          <item value="1" alpha="255" label="&lt;= 1" color="#fde725"/>
          <item value="5" alpha="255" label="1 - 5" color="#5dc963"/>
          <item value="10" alpha="255" label="5 - 10" color="#26818e"/>
          <item value="inf" alpha="255" label="> 10" color="#440154"/>
          <rampLegendSettings maximumLabel="" orientation="2" prefix="" direction="0" useContinuousLegend="1" minimumLabel="" suffix="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option name="decimal_separator" value="" type="QChar"/>
                <Option name="decimals" value="6" type="int"/>
                <Option name="rounding_type" value="0" type="int"/>
                <Option name="show_plus" value="false" type="bool"/>
                <Option name="show_thousand_separator" value="true" type="bool"/>
                <Option name="show_trailing_zeros" value="false" type="bool"/>
                <Option name="thousand_separator" value="" type="QChar"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast brightness="0" gamma="1" contrast="0"/>
    <huesaturation colorizeOn="0" grayscaleMode="0" colorizeGreen="128" colorizeStrength="100" colorizeBlue="128" invertColors="0" saturation="0" colorizeRed="255"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
