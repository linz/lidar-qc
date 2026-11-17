<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="Symbology" version="3.44.7-Solothurn">
  <pipe-data-defined-properties>
    <Option type="Map">
      <Option type="QString" value="" name="name"/>
      <Option name="properties"/>
      <Option type="QString" value="collection" name="type"/>
    </Option>
  </pipe-data-defined-properties>
  <pipe>
    <provider>
      <resampling zoomedInResamplingMethod="nearestNeighbour" zoomedOutResamplingMethod="nearestNeighbour" enabled="false" maxOversampling="2"/>
    </provider>
    <rasterrenderer type="singlebandpseudocolor" nodataColor="255,0,0,0,rgb:1,0,0,0" alphaBand="-1" opacity="1" classificationMin="0" classificationMax="8" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Exact</statAccuracy>
        <cumulativeCutLower>0</cumulativeCutLower>
        <cumulativeCutUpper>1</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" minimumValue="0" clip="0" maximumValue="8" labelPrecision="0">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option type="QString" value="0,0,0,0,rgb:0,0,0,0" name="color1"/>
              <Option type="QString" value="26,152,80,255,rgb:0.1019608,0.5960784,0.3137255,1" name="color2"/>
              <Option type="QString" value="ccw" name="direction"/>
              <Option type="QString" value="0" name="discrete"/>
              <Option type="QString" value="gradient" name="rampType"/>
              <Option type="QString" value="rgb" name="spec"/>
              <Option type="QString" value="0.125;215,0,3,255,hsv:0.99736111111111114,1,0.84313725490196079,1;rgb;ccw:0.234375;215,0,3,255,hsv:0.99736111111111114,1,0.84313725490196079,1;rgb;ccw:0.375;215,0,3,255,hsv:0.99736111111111114,1,0.84313725490196079,1;rgb;ccw:0.453125;254,224,139,255,rgb:0.9960784,0.8784314,0.545098,1;rgb;ccw:0.671875;254,224,139,255,rgb:0.9960784,0.8784314,0.545098,1;rgb;ccw:0.890625;254,224,139,255,rgb:0.9960784,0.8784314,0.545098,1;rgb;ccw" name="stops"/>
            </Option>
          </colorramp>
          <item value="0" label="0" color="#000000" alpha="0"/>
          <item value="1" label="1" color="#d70003" alpha="255"/>
          <item value="1.875" label="2" color="#d70003" alpha="255"/>
          <item value="3" label="3" color="#d70003" alpha="255"/>
          <item value="3.625" label="4" color="#fee08b" alpha="255"/>
          <item value="5.375" label="5" color="#fee08b" alpha="255"/>
          <item value="7.125" label="7" color="#fee08b" alpha="255"/>
          <item value="8" label="8" color="#1a9850" alpha="255"/>
          <rampLegendSettings suffix="" direction="0" orientation="2" maximumLabel="" useContinuousLegend="1" minimumLabel="" prefix="">
            <numericFormat id="basic">
              <Option type="Map">
                <Option type="invalid" name="decimal_separator"/>
                <Option type="int" value="6" name="decimals"/>
                <Option type="int" value="0" name="rounding_type"/>
                <Option type="bool" value="false" name="show_plus"/>
                <Option type="bool" value="true" name="show_thousand_separator"/>
                <Option type="bool" value="false" name="show_trailing_zeros"/>
                <Option type="invalid" name="thousand_separator"/>
              </Option>
            </numericFormat>
          </rampLegendSettings>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0" gamma="1"/>
    <huesaturation saturation="0" colorizeOn="0" grayscaleMode="0" colorizeGreen="128" colorizeStrength="100" colorizeBlue="128" colorizeRed="255" invertColors="0"/>
    <rasterresampler maxOversampling="2"/>
    <resamplingStage>resamplingFilter</resamplingStage>
  </pipe>
  <blendMode>0</blendMode>
</qgis>
