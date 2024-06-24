RSpec.describe RubySMB::Dcerpc::PrintSystem::RpcAddPrinterDriverExResponse do
  subject(:packet) { described_class.new }

  it { is_expected.to respond_to :error_status }

  it 'is little endian' do
    expect(described_class.fields.instance_variable_get(:@hints)[:endian]).to eq :little
  end

  describe '#error_status' do
    it 'is a NdrUint32' do
      expect(packet.error_status).to be_a RubySMB::Dcerpc::Ndr::NdrUint32
    end
  end

  describe '#initialize_instance' do
    it 'sets #opnum to RPC_ADD_PRINTER_DRIVER_EX constant' do
      expect(packet.opnum).to eq(RubySMB::Dcerpc::PrintSystem::RPC_ADD_PRINTER_DRIVER_EX)
    end
  end

  it 'reads its own binary representation and outputs the same packet' do
    packet = described_class.new(
      error_status: 0
    )
    binary = packet.to_binary_s
    expect(described_class.read(binary)).to eq(packet)
  end
end

