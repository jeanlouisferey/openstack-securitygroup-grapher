# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0]

### Added

- this changelog file
- New markdown and csv output
- Abbility to filter instances and security groups name
- Abbility to show or not egress ANY ANY rules
- Abbility to graph security groups attached to interfaces (useful for instances with multiple ports with different security groups on each ports)
- Documentation of new features

### Changed
- Ansible 2.9 compatibility
- Use of openstack.cloud collection

### Removed
- Specific Ansible module to get security groups rules facts

## [1.0.0]

### Added

- First official version
