# -*- coding: binary -*-

require 'English'
require 'rex/ui/text/dispatcher_shell'

module Rex
  module Post
    module LDAP
      module Ui
        ###
        #
        # Base class for all command dispatchers within the LDAP console user
        # interface.
        #
        ###
        module Console::CommandDispatcher
          include Msf::Ui::Console::CommandDispatcher::Session

          #
          # Initializes an instance of the core command set using the supplied session and client
          # for interactivity.
          #
          # @param [Rex::Post::LDAP::Ui::Console] console
          def initialize(console)
            super
            @msf_loaded = nil
            @filtered_commands = []
          end

          #
          # Returns the LDAP client context.
          #
          # @return [Rex::Proto::LDAP::Client]
          def client
            console = shell
            console.client
          end

          #
          # Returns the LDAP session context.
          #
          # @return [Msf::Sessions::LDAP]
          def session
            console = shell
            console.session
          end

          #
          # Returns the commands that meet the requirements
          #
          def filter_commands(all, reqs)
            all.delete_if do |cmd, _desc|
              if reqs[cmd]&.any? { |req| !client.commands.include?(req) }
                @filtered_commands << cmd
                true
              end
            end
          end

          def unknown_command(cmd, line)
            if @filtered_commands.include?(cmd)
              print_error("The \"#{cmd}\" command is not supported by this session type (#{session.session_type})")
              return :handled
            end

            super
          end

          #
          # Return the subdir of the `documentation/` directory that should be used
          # to find usage documentation
          #
          def docs_dir
            File.join(super, 'ldap_session')
          end

          #
          # Returns true if the client has a framework object.
          #
          # Used for firing framework session events
          #
          def msf_loaded?
            return @msf_loaded unless @msf_loaded.nil?

            # if we get here we must not have initialized yet

            @msf_loaded = !session.framework.nil?
            @msf_loaded
          end

          #
          # Log that an error occurred.
          #
          def log_error(msg)
            print_error(msg)

            elog(msg, 'ldap')

            dlog("Call stack:\n#{$ERROR_POSITION.join("\n")}", 'ldap')
          end
        end
      end
    end
  end
end
