# -*- encoding: utf-8 -*-
# stub: allure-ruby-commons 2.24.5 ruby lib

Gem::Specification.new do |s|
  s.name = "allure-ruby-commons".freeze
  s.version = "2.24.5".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.metadata = { "bug_tracker_uri" => "https://github.com/allure-framework/allure-ruby/issues", "changelog_uri" => "https://github.com/allure-framework/allure-ruby/releases", "documentation_uri" => "https://github.com/allure-framework/allure-ruby/blob/master/allure-ruby-commons/README.md", "rubygems_mfa_required" => "false", "source_code_uri" => "https://github.com/allure-framework/allure-ruby/tree/master/allure-ruby-commons", "wiki_uri" => "https://github.com/allure-framework/allure-ruby/wiki" } if s.respond_to? :metadata=
  s.require_paths = ["lib".freeze]
  s.authors = ["Andrejs Cunskis".freeze]
  s.date = "2024-05-06"
  s.description = "Utilities allowing to implement allure result generation by other test frameworks".freeze
  s.email = "andrejs.cunskis@gmail.com".freeze
  s.homepage = "https://github.com/allure-framework/allure-ruby".freeze
  s.licenses = ["Apache-2.0".freeze]
  s.required_ruby_version = Gem::Requirement.new(">= 3.0.0".freeze)
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Common library for allure results generation".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_runtime_dependency(%q<mime-types>.freeze, [">= 3.3".freeze, "< 4".freeze])
  s.add_runtime_dependency(%q<require_all>.freeze, [">= 2".freeze, "< 4".freeze])
  s.add_runtime_dependency(%q<rspec-expectations>.freeze, ["~> 3.12".freeze])
  s.add_runtime_dependency(%q<uuid>.freeze, [">= 2.3".freeze, "< 3".freeze])
end
