module RubySMB
  module Dcerpc
    module PrintSystem

      # [3.1.4.4.2 RpcEnumPrinterDrivers (Opnum 10)](https://docs.microsoft.com/en-us/openspecs/windows_protocols/ms-rprn/857d00ac-3682-4a0d-86ca-3d3c372e5e4a)
      class RpcEnumPrinterDriversResponse < BinData::Record
        attr_reader :opnum

        endian :little

        def initialize_instance
          super
          @opnum = RPC_ENUM_PRINTER_DRIVERS
        end

        rprn_byte_array_ptr  :p_drivers
        ndr_uint32           :pcb_needed
        ndr_uint32           :pc_returned
        ndr_uint32           :error_status
      end
    end
  end
end
