# -*- encoding: utf-8 -*-
# stub: rex-random_identifier 0.1.12 ruby lib

Gem::Specification.new do |s|
  s.name = "rex-random_identifier".freeze
  s.version = "0.1.12".freeze

  s.required_rubygems_version = Gem::Requirement.new(">= 0".freeze) if s.respond_to? :required_rubygems_version=
  s.require_paths = ["lib".freeze]
  s.authors = ["Metasploit Hackers".freeze]
  s.cert_chain = ["-----BEGIN CERTIFICATE-----\nMIIERDCCAqygAwIBAgIBATANBgkqhkiG9w0BAQsFADAmMSQwIgYDVQQDDBttc2Zk\nZXYvREM9bWV0YXNwbG9pdC9EQz1jb20wHhcNMjMxMDMwMTYwNDI1WhcNMjUxMDI5\nMTYwNDI1WjAmMSQwIgYDVQQDDBttc2ZkZXYvREM9bWV0YXNwbG9pdC9EQz1jb20w\nggGiMA0GCSqGSIb3DQEBAQUAA4IBjwAwggGKAoIBgQDZN/EKv+yVjwiKWvjAVhjF\naWNYI0E9bJ5d1qKd29omRYX9a+OOKBCu5+394fyF5RjwU4mYGr2iopX9ixRJrWXH\nojs70tEvV1CmvP9rhz7JKzQQoJOkinrz4d+StIylxVxVdgm7DeiB3ruTwvl7qKUv\npiWzhrBFiVU6XIEAwq6wNEmnv2D+Omyf4h0Tf99hc6G0QmBnU3XydqvnZ+AzUbBV\n24RH3+NQoigLbvK4M5aOeYhk19di58hznebOw6twHzNczshrBeMFQp985ScNgsvF\nrL+7HNNwpcpngERwZfzDNn7iYN5X3cyvTcykShtsuPMa5zXsYo42LZrsTF87DW38\nD8sxL6Dgdqu25Mltdw9m+iD4rHSfb1KJYEoNO+WwBJLO2Y4d6G1CR66tVeWsZspb\nzneOVC+sDuil7hOm+6a7Y2yrrRyT6IfL/07DywjPAIRUp5+Jn8ZrkWRNo2AOwWBG\nk5gz7SfJPHuyVnPlxoMA0MTFCUnnnbyHu882TGoJGgMCAwEAAaN9MHswCQYDVR0T\nBAIwADALBgNVHQ8EBAMCBLAwHQYDVR0OBBYEFIQfNa4E889ZE334cwU7eNu2hScH\nMCAGA1UdEQQZMBeBFW1zZmRldkBtZXRhc3Bsb2l0LmNvbTAgBgNVHRIEGTAXgRVt\nc2ZkZXZAbWV0YXNwbG9pdC5jb20wDQYJKoZIhvcNAQELBQADggGBAMfzvKcV27p7\npctmpW2JmIXLMrjNLyGJAxELH/t9pJueXdga7uj2fJkYQDbwGw5x4MGyFqhqJLH4\nl/qsUF3PyAXDTSWLVaqXQVWO+IIHxecG0XjPXTNudzMU0hzqbqiBKvsW7/a3V5BP\nSWlFzrFkoXWlPouFpoakyYMJjpW4SGdPzRv7pM4OhXtkXpHiRvx5985FrHgHlI89\nNSIuIUbp8zqk4hP1i9MV0Lc/vTf2gOmo+RHnjqG1NiYfMCYyY/Mcd4W36kGOl468\nI8VDTwgCufkAzFu7BJ5yCOueqtDcuq+d3YhAyU7NI4+Ja8EwazOnB+07sWhKpg7z\nyuQ1mWYPmZfVQpoSVv1CvXsoqJYXVPBBLOacKKSj8ArVG6pPn9Bej7IOQdblaFjl\nDgscAao7wB3xW2BWEp1KnaDWkf1x9ttgoBEYyuYwU7uatB67kBQG1PKvLt79wHvz\nDxs+KOjGbBRfMnPgVGYkORKVrZIwlaboHbDKxcVW5xv+oZc7KYXWGg==\n-----END CERTIFICATE-----\n".freeze]
  s.date = "2024-05-13"
  s.description = "Ruby Exploitation(Rex) library for generating Random identifier strings".freeze
  s.email = ["msfdev@metasploit.com".freeze]
  s.homepage = "https://github.com/rapid7/rex-random_identifier".freeze
  s.required_ruby_version = Gem::Requirement.new(">= 2.2.0".freeze)
  s.rubygems_version = "3.5.10".freeze
  s.summary = "Random Identifier Generator".freeze

  s.installed_by_version = "3.5.10".freeze if s.respond_to? :installed_by_version

  s.specification_version = 4

  s.add_development_dependency(%q<rake>.freeze, [">= 0".freeze])
  s.add_development_dependency(%q<rspec>.freeze, [">= 0".freeze])
  s.add_runtime_dependency(%q<rex-text>.freeze, [">= 0".freeze])
end
