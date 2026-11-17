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
    <rasterrenderer type="singlebandpseudocolor" nodataColor="" alphaBand="-1" opacity="1" classificationMin="0" classificationMax="2" band="1">
      <rasterTransparency>
        <singleValuePixelList>
          <pixelListEntry min="0" max="0" percentTransparent="100"/>
        </singleValuePixelList>
      </rasterTransparency>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader colorRampType="INTERPOLATED" classificationMode="1" minimumValue="0" clip="0" maximumValue="2" labelPrecision="2">
          <colorramp type="gradient" name="[source]">
            <Option type="Map">
              <Option type="QString" value="48,18,59,255,rgb:0.1882353,0.0705882,0.2313725,1" name="color1"/>
              <Option type="QString" value="122,4,3,255,rgb:0.4784314,0.0156863,0.0117647,1" name="color2"/>
              <Option type="QString" value="ccw" name="direction"/>
              <Option type="QString" value="0" name="discrete"/>
              <Option type="QString" value="gradient" name="rampType"/>
              <Option type="QString" value="rgb" name="spec"/>
              <Option type="QString" value="0.111111;70,98,215,255;rgb;ccw:0.222222;54,170,249,255;rgb;ccw:0.333333;26,228,182,255;rgb;ccw:0.444444;114,254,94,255;rgb;ccw:0.555556;200,239,52,255;rgb;ccw:0.666667;250,186,57,255;rgb;ccw:0.777778;246,107,25,255;rgb;ccw:0.888889;202,42,4,255;rgb;ccw" name="stops"/>
            </Option>
          </colorramp>
          <item value="0" label="0" color="#30123b" alpha="255"/>
          <item value="0.2222" label="0.22" color="#4662d7" alpha="255"/>
          <item value="0.4444" label="0.44" color="#36aaf9" alpha="255"/>
          <item value="0.6667" label="0.67" color="#1ae4b6" alpha="255"/>
          <item value="0.8889" label="0.89" color="#72fe5e" alpha="255"/>
          <item value="1.1111" label="1.11" color="#c8ef34" alpha="255"/>
          <item value="1.3333" label="1.33" color="#faba39" alpha="255"/>
          <item value="1.5556" label="1.56" color="#f66b19" alpha="255"/>
          <item value="1.7778" label="1.78" color="#ca2a04" alpha="255"/>
          <item value="2" label="2 m" color="#7a0403" alpha="255"/>
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
