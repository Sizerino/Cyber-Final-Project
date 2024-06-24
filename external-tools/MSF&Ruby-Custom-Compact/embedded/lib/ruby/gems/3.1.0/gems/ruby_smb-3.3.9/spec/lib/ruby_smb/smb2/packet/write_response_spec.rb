require 'spec_helper'

RSpec.describe RubySMB::SMB2::Packet::WriteResponse do
  subject(:packet) { described_class.new }

  it { is_expected.to respond_to :smb2_header }
  it { is_expected.to respond_to :structure_size }
  it { is_expected.to respond_to :write_count }
  it { is_expected.to respond_to :remaining_bytes }
  it { is_expected.to respond_to :channel_offset }
  it { is_expected.to respond_to :channel_length }


  it 'is little endian' do
    expect(described_class.fields.instance_variable_get(:@hints)[:endian]).to eq :little
  end

  describe '#smb2_header' do
    subject(:header) { packet.smb2_header }

    it 'is a standard SMB Header' do
      expect(header).to be_a RubySMB::SMB2::SMB2Header
    end

    it 'should have the command set to SMB_COM_NEGOTIATE' do
      expect(header.command).to eq RubySMB::SMB2::Commands::WRITE
    end

    it 'should have the response flag set' do
      expect(header.flags.reply).to eq 1
    end
  end

  it 'should have a structure size of 49' do
    expect(packet.structure_size).to eq 17
  end

end
