<div align="center">

<p>
    <a href="https://github.com/ArtixLabs/Niagara/releases/latest">
      <img alt="Latest release" src="https://img.shields.io/github/v/release/ArtixLabs/Niagara?style=for-the-badge&logo=starship&color=C9CBFF&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/ArtixLabs/Niagara/pulse">
      <img alt="Last commit" src="https://img.shields.io/github/last-commit/ArtixLabs/Niagara?style=for-the-badge&logo=starship&color=8bd5ca&logoColor=D9E0EE&labelColor=302D41"/>
    </a>
    <a href="https://github.com/ArtixLabs/Niagara/blob/master/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/ArtixLabs/Niagara?style=for-the-badge&logo=starship&color=ee999f&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/ArtixLabs/Niagara/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/ArtixLabs/Niagara?style=for-the-badge&logo=starship&color=c69ff5&logoColor=D9E0EE&labelColor=302D41" />
    </a>
    <a href="https://github.com/ArtixLabs/Niagara/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/ArtixLabs/Niagara?style=for-the-badge&logo=bilibili&color=F5E0DC&logoColor=D9E0EE&labelColor=302D41" />
    </a>
</div>

## Niagara

Niagara is a ricing tool made for Linux systems. It aims to be a universal tool that can be used on multiple distributions, as it does not rely on a singular package manager. Niagara manages configs by taking a JSON file that contains some fields such as `packages`, `dotfile`, `wallpaper`, etc. 

### How does Niagara handle packages?

Niagara has a list of packages that you can place inside the configuration file, and then it goes and checks it against the corresponding package for your linux distribution. A good example would be the following:

```json
{
    "name": "doas",
    "arch": "opendoas",
    "void": "opendoas",
    "fedora": "opendoas",
    "gentoo": "app-admin/doas"
}
```

This allows us to support multiple distributions, whilst making it a *write once, run anywhere* style of program.

## Features

- packages
- config
  - wallpaper
  - dotfile
  - scripts
  - commands
    - available to clone and use a git repository as the basis for commands
    - option to run the command in a specified directory
- xinitrc generation

## Example configuration

```json
{
  "packages": [
    "sway",
    "feh",
    "picom",
    "i3",
    "kitty"
  ],
  "config": [
    {
      "option": "wallpaper",
      "val": "https://github.com/kavulox/dotfiles/raw/master/wallpapers/forest.jpg"
    },
    {
      "option": "dotfile",
      "val": [
        "https://github.com/kavulox/nvim",
        "https://github.com/kavulox/picom"
      ]
    },
    {
      "option": "scripts",
      "val": [
        {
          "method": "curl",
          "url": "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh"
        }
      ]
    }
  ],
  "source": [
    {
      "link": "https://git.suckless.org/dwm",
      "cmds": [
        {
          "dir": "dwm",
          "cmd": "sudo make clean install"
        }
      ]
    }
  ],
  "xinitrc": [
    "picom -b",
    "exec dwm"
  ]
}
```

## Contributing

New contributors should submit a PR with a short description of their changes.

## ArtixLabs

Join our discord server at https://discord.gg/ajNswSyf6q

Join our Matrix space at https://matrix.to/#/#artixlabs:halogen.city

## Todo

- Get more packages.
  - Make packages support multiple package managers.
- Split deps.py into multiple files.
- Add documentation.
- Add checks to see if a specified package is not natively available for a distribution, then to refer to a custom build option.


## Author

**Niagara** was written by kavulox
