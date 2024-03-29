<p align="left" >
<a href='https://carbonplan.org'>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://carbonplan-assets.s3.amazonaws.com/monogram/light-small.png">
  <img alt="CarbonPlan monogram." height="48" src="https://carbonplan-assets.s3.amazonaws.com/monogram/dark-small.png">
</picture>
</a>
</p>

# toucan-crypto-offsets
Code and data underlying CarbonPlan's article entitle "Zombies on the blockchain."

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

This CarbonPlan repository contains all the code and data necessary to recreate the figures and findings reported in our research article entitled "Zombies on the blockchain."
In addition to containing a script for downloading Verra transaction data, we also include a manually compiled list of Verra project registration dates.
Together, these data allow us to take stock of the types of Verra offset credits that have been bridge via the Toucan protocol.
The `data/` folder contains a static copy of all data used in our analysis.

The analysis is contained entirely within a single Jupyter notebook, `core-analysis.ipynb`.
That code i) identifies all projects that have reported retirements via Toucan and ii) classifies projects as being "zombies."
A project qualifies as being a zombie project if it meets one of two criteria:
- The project has transacted more than 95 percent if its retirements via Toucan
- The project had not seen a retirement in the two years prior to its first Toucan retirment.


## license

All the code in this repository is [MIT](https://choosealicense.com/licenses/mit/)-licensed, but we request that you please provide attribution if reusing any of our digital content (graphics, logo, articles, etc.).

## about us

CarbonPlan is a nonprofit organization that uses data and science for climate action.
We aim to improve the transparency and scientific integrity of climate solutions with open data and tools. Find out more at [carbonplan.org](https://carbonplan.org/) or get in touch by [opening an issue](https://github.com/carbonplan/toucan-crypto-offsets/issues/new) or [sending us an email](mailto:hello@carbonplan.org).
