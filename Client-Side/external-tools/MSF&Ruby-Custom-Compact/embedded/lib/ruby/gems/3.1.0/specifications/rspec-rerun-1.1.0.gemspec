# -*- encoding: utf-8 -*-
# stub: rspec-rerun 1.1.0 ruby lib

Gem::Specification.new do |s|
  s.name = "rspec-rerun".freeze
  s.version = "1.1.0".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Daniel Doubrovkine".freeze]
  s.date = "2015-07-02"
  s.email = "dblock@dblock.org".freeze
  s.homepage = "https://github.com/dblock/rspec-rerun".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Re-run failed RSpec tests.".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_runtime_dependency(%q<rspec>.freeze, ["~> 3.0".freeze])
  s.add_development_dependency(%q<rake>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<bundler>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<rubocop>.freeze, ["= 0.31.0".freeze])
  s.add_development_dependency(%q<bump>.freeze, [">= 0".freeze])
end
