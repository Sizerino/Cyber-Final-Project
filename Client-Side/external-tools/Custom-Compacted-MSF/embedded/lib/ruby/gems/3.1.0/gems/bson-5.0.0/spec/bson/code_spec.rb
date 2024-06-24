# rubocop:todo all
# Copyright (C) 2009-2020 MongoDB Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

require "spec_helper"

describe BSON::Code do

  describe "#as_extended_json" do

    let(:object) do
      described_class.new("this.value = 5")
    end

    it "returns the binary data plus type" do
      expect(object.as_extended_json).to eq({ "$code" => "this.value = 5" })
    end

    it_behaves_like 'an Extended JSON serializable object'
    it_behaves_like '#as_json calls #as_extended_json'
  end

  describe "#to_bson/#from_bson" do

    let(:type) { 13.chr }
    let(:obj)  { described_class.new("this.value = 5") }
    let(:bson) { "#{15.to_bson}this.value = 5#{BSON::NULL_BYTE}" }

    it_behaves_like "a bson element"
    it_behaves_like "a serializable bson element"
    it_behaves_like "a deserializable bson element"
  end
end
