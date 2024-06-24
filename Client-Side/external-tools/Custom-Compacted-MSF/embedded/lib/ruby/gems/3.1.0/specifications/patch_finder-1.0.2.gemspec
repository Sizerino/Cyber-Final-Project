# -*- encoding: utf-8 -*-
# stub: patch_finder 1.0.2 ruby lib

Gem::Specification.new do |s|
  s.name = "patch_finder".freeze
  s.version = "1.0.2".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["wchen-r7".freeze]
  s.date = "2016-03-30"
  s.description = "Generic Patch Finder".freeze
  s.email = ["wei_chen@rapid7.com".freeze]
  s.executables = ["msu_finder".freeze]
  s.files = ["bin/msu_finder".freeze]
  s.homepage = "http://github.com/wchen-r7/patch-finder".freeze
  s.licenses = ["BSD-3-clause".freeze]
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Patch Finder".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_development_dependency(%q<bundler>.freeze, ["~> 1.11".freeze])
  s.add_development_dependency(%q<rake>.freeze, ["~> 10.0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0".freeze])
end
