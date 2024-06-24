# -*- encoding: utf-8 -*-
# stub: aarch64 2.1.0 ruby lib

Gem::Specification.new do |s|
  s.name = "aarch64".freeze
  s.version = "2.1.0".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Aaron Patterson".freeze]
  s.date = "2024-04-29"
  s.description = "Tired of writing Ruby in Ruby? Now you can write ARM64 assembly in Ruby!".freeze
  s.email = "tenderlove@ruby-lang.org".freeze
  s.homepage = "https://github.com/tenderlove/aarch64".freeze
  s.licenses = ["Apache-2.0".freeze]
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Write ARM64 assembly in Ruby!".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_runtime_dependency(%q<racc>.freeze, ["~> 1.6".freeze])
  s.add_development_dependency(%q<hatstone>.freeze, ["~> 1.0.0".freeze])
  s.add_development_dependency(%q<jit_buffer>.freeze, ["~> 1.0.0".freeze])
  s.add_development_dependency(%q<minitest>.freeze, ["~> 5.15".freeze])
  s.add_development_dependency(%q<rake>.freeze, ["~> 13.0".freeze])
  s.add_development_dependency(%q<odinflex>.freeze, ["~> 1.0".freeze])
end
