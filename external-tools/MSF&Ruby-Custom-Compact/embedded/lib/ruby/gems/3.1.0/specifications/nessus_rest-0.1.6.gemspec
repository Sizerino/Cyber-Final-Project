# -*- encoding: utf-8 -*-
# stub: nessus_rest 0.1.6 ruby lib

Gem::Specification.new do |s|
  s.name = "nessus_rest".freeze
  s.version = "0.1.6".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Vlatko Kosturjak".freeze]
  s.date = "2016-09-20"
  s.description = "Ruby library for Nessus (version 6+) JSON/REST interface. This library is used for communication with Nessus over REST interface. You can start, stop, pause and resume scan. Watch progress and status of scan, download report, etc. ".freeze
  s.email = "vlatko.kosturjak@gmail.com".freeze
  s.homepage = "https://github.com/kost/nessus_rest-ruby".freeze
  s.licenses = ["MIT".freeze]
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Communicate with Nessus Scanner (version 6+) over REST/JSON interface".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 3

  s.add_development_dependency(%q<bundler>.freeze, [">= 1.1".freeze])
  s.add_development_dependency(%q<pry>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<rake>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<yard>.freeze, [">= 0".freeze])
end
