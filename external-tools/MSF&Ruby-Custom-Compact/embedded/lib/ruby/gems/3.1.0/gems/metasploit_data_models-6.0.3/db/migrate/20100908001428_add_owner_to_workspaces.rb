class AddOwnerToWorkspaces < ActiveRecord::Migration[4.2]
  def self.up
    add_column :workspaces, :owner_id, :integer
  end

  def self.down
    remove_column :workspaces, :owner_id
  end
end
