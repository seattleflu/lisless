# Lisless

Lisless is a non-[LIS][] for those without one: the LIS-less.  It is a
LIS-in-name-only that does less.

**This is a work-in-progress prototype.**  The plan is that Lisless will
receive [ASTM E1381/1394][ASTM] test results from laboratory instruments and
convert them to [FHIR v4][] documents for other data systems to process.

The [Seattle Flu Study][] has a number of data systems, including our own
[ID3C][] and [NWGC][]'s "Samplify" LIMS (which [isn't a LIS][LIMSvLIS]), but
none of them speak [HL7 v2/3][HL7] or [ASTM E1381/1394][ASTM].  These protocols
are commonly used by clinical-grade laboratory instruments to report results
directly to a hospital LIS and onwards into the medical record.  As the Study
starts to use [Cepheid's GeneXpert instruments][cepheid] to test samples, we
want to use the instruments' LIS-integration capabilities to capture results
automatically instead of parsing PDF exports or manual data entry.

[LIS]: https://en.wikipedia.org/wiki/Laboratory_information_system
[ID3C]: https://github.com/seattleflu/id3c
[NWGC]: https://nwgc.gs.washington.edu/
[LIMSvLIS]: https://en.wikipedia.org/wiki/Laboratory_information_management_system#Distinction_between_a_LIMS_and_a_LIS
[HL7]: https://en.wikipedia.org/wiki/Health_Level_7
[ASTM]: https://www.astm.org/Standards/E1394.htm
[FHIR v4]: http://www.hl7.org/implement/standards/fhir/
[cepheid]: https://www.cepheid.com/en_US/systems/GeneXpert-Family-of-Systems/GeneXpert-System
[Seattle Flu Study]: https://seattleflu.org
