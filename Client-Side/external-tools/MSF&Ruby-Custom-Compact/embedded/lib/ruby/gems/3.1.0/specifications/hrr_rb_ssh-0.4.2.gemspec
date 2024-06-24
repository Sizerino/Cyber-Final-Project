# -*- encoding: utf-8 -*-
# stub: hrr_rb_ssh 0.4.2 ruby lib

Gem::Specification.new do |s|
  s.name = "hrr_rb_ssh".freeze
  s.version = "0.4.2".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["hirura".freeze]
  s.date = "2020-01-20"
  s.description = "Pure Ruby SSH 2.0 server and client implementation".freeze
  s.email = ["hirura@gmail.com".freeze]
  s.homepage = "https://github.com/hirura/hrr_rb_ssh".freeze
  s.licenses = ["Apache-2.0".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 2.0.0".freeze)
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Pure Ruby SSH 2.0 server and client implementation".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_development_dependency(%q<rake>.freeze, ["~> 12.0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, ["~> 3.0".freeze])
  s.add_development_dependency(%q<simplecov>.freeze, ["~> 0.16".freeze])
end
