This is a collection of various response matrices used at OCL/the nuclear physics group in Oslo.

Files:
- `oscar2020`: OSCAR response from the simulations from 2020 in 16cm distance configuraton, 28 dectors, with the new taget chamber. Calculated on 10 keV grid between 50 keV and 10 MeV. Reference to article will follow. Based on OCL_GEANT4 v2.0.0; See [response_results](https://github.com/oslocyclotronlab/OCL_GEANT4/releases/tag/v2.0.0) for other formats and the response > 10 MeV. 
  - `_norm_efficiency`: spectra for each incident energy are normalized to the 
    total efficiency (equals division by number of incident events)
  - `_norm_1`: spectra for each incident energy are normalized to 1
- `oscar2017_scale1.15`: (Old) OSCAR response from the simulations in 2017, actinide target chamber, 24(?) cm distance. The cmp. part is scaled up by 1.15 to get a better match with the (analoge) in-beam spectra. See [arxiv/2008.06240v1](https://arxiv.org/abs/2008.06240v1) for more information. Based on OCL_GEANT4 v1.0.3.
- `nai2012_for_opt13`: CACTUS response matrix as remeasured 2012
- `nai2012_alternative_format.zip`: CACTUS response, as above, `nai2012_for_opt13` but in zip format
  
Further files:
- `test_response_interpolation_cactus.py`: Some test, not sure what it does
