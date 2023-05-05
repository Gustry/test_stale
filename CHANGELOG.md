# Changelog BOB

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [10.0.0] - 2019-09-11

* Fix quadratic parse time for some combinations of pairs, #583. Algorithm is
  now similar to one in reference implementation.
* Deps bump.


## [9.1.0] - 2019-08-11

### Added

* Remove extra characters from line break check. Leave only 0x0A & 0x0D, as in
  CommonMark spec, #581.

### Fixed

* Something

## [9.0.1] - 2019-07-12

* Fix possible corruption of open/close tag levels, #466


## [9.0.0] - 2019-07-09

* Updated CM spec compatibility to 0.29.
* Update Travis-CI node version to actual (8 & latest).
* Deps bump.

##
