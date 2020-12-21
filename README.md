# Response function at OCL
This is a collection of various response matrices used at OCL/the nuclear physics group in Oslo.

Files:
- `oscar2020`: OSCAR response from the simulations from 2020 in 16 cm distance configuration, 30 detectors, with the new target chamber. Calculated on 10 keV grid between 50 keV and 10 MeV. Reference to article will follow. Based on OCL_GEANT4 v2.0.0; See [response_results](https://github.com/oslocyclotronlab/OCL_GEANT4/releases/tag/v2.0.0) for other formats and the response > 10 MeV. 
  - `_norm_efficiency`: spectra for each incident energy are normalized to the 
    total efficiency (equals division by number of incident events)
  - `_norm_1`: spectra for each incident energy are normalized to 1
  - `mama_export.zip`: Files needed for interpolation of response within mama 
    (unzip first); alternative to usage of response matrix above directly 
  - `ompy_interpolate.zip`: Files needed for interpolation of response within ompy 
    (unzip first); alternative to usage of response matrix above directly 
- `oscar2017_scale1.15`: (Old) OSCAR response from the simulations in 2017, actinide target chamber, 24(?) cm distance. The cmp. part is scaled up by 1.15 to get a better match with the (analogue) in-beam spectra. See [arxiv/2008.06240v1 (v1)](https://arxiv.org/abs/2008.06240v1) for more information. Based on OCL_GEANT4 v1.0.3.
- `nai2012_for_opt13`: CACTUS response matrix as remeasured 2012
- `nai2012_alternative_format.zip`: CACTUS response, as above, `nai2012_for_opt13` but in zip format
  
Further files:
- `test_response_interpolation_cactus.py`: Some test, not sure what it does

## How to cite:
- `oscar2020`: Cite the article [Zeiser2020, DOI: 10.1016/j.nima.2020.164678](https://doi.org/10.1016/j.nima.2020.164678) *and*, if possible, also the DOI of the specific version of the response you use / the files, i.e. zenodo e.g. via 
[DOI: 10.5281/zenodo.4018494](https://doi.org/10.5281/zenodo.4018494)
 for v2.0.0.1.
- `oscar2017_scale1.15`: Cite the arXive article (v1) [arxiv/2008.06240v1](https://arxiv.org/abs/2008.06240v1) and the correct zenodo version v1.0.3 (10.5281/zenodo.1339347). We appreciate if you also cite the published article, [DOI: 10.1016/j.nima.2020.164678](https://doi.org/10.1016/j.nima.2020.164678), which very briefly discusses the challenges and changes that occurred since v1.0.3. Citing the article will also give us, the programmers, creds.
- `nai2012_for_opt13` and `nai2012_alternative_format.zip`: No clear guideline. The response procedure was outlined in [Guttormsen (1996)](https://doi.org/10.1016/0168-9002(96)00197-0) and the response was remeasured as explained in [Crespo Campo (2016)](https://doi.org/10.1103/PhysRevC.94.044321). Potentially cite this github page (+ access date and/or commit).

For the OSCAR response, you may also have a look at the corresponding github [OCL_GEANT4](https://github.com/oslocyclotronlab/OCL_GEANT4/).
