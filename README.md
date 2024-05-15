# Dotipe

Dotipe is an orchestration tool for managing your dotfiles. It is a simple tool that allows you to manage your dotfiles 
in a git repository and deploy them to your home directory.

When this project is executed, it will cover all the dotfiles in the toml looking for any changes.
If there is a change, it will show you that you will need to update the dotfile in the repository.
Today, I don't want to do an implementation to make this tool update the dotfiles in the repository,
so it should be done manually.

Another feature is: This tool should work as a backup tool for your dotfiles.
So, if you have a clean system installation, it should help you to restore your dotfiles, downloading 
them from the repository.

---

## How it works
In your home folder, this tool will create a `toml` file like the one below:

```toml
[user]
info = "Do not edit this [user] session"
os = "Linux"

[wsl]
raw_url = "https://example.com"
file_name = "test_file"
file_path = "/Downloads/"
````

The section is the dotfile itself
the attributes is the metadata of the dotfile

The `raw_url` is the raw url of the dotfile
The `file_name` is the name of the file
The `file_path` is the path where the file or folder should be
