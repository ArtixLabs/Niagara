import os

templ = """
{
  "packages": [
    {
      "pkgname": "picom",
      "arch": "picom",
      "void": "picom"
    },
    {
      "pkgname": "kitty",
      "arch": "kitty",
      "void": "kitty"
    },
    {
      "pkgname": "alacritty",
      "arch": "alacritty",
      "void": "alacritty"
    },
    {
      "pkgname": "neofetch",
      "arch": "neofetch",
      "void": "neofetch"
    },
    {
      "pkgname": "feh",
      "arch": "feh",
      "void": "feh"
    },
    {
      "pkgname": "emacs",
      "arch": "emacs",
      "void": "emacs"
    },
    {
      "pkgname": "vim",
      "arch": "vim",
      "void": "vim"
    },
    {
      "pkgname": "neovim",
      "arch": "neovim",
      "void": "neovim"
    },
    {
      "pkgname": "rofi",
      "arch": "rofi",
      "void": "rofi"
    },
    {
      "pkgname": "flameshot",
      "arch": "flameshot",
      "void": "flameshot"
    },
    {
      "pkgname": "doas",
      "arch": "opendoas",
      "void": "opendoas"
    },
    {
      "pkgname": "dunst",
      "arch": "dunst",
      "void": "dunst"
    },
    {
      "pkgname": "firefox",
      "arch": "firefox",
      "void": "firefox"
    },
    {
      "pkgname": "ripgrep",
      "arch": "ripgrep",
      "void": "ripgrep"
    },
    {
      "pkgname": "mpv",
      "arch": "mpv",
      "void": "mpv"
    },
    {
      "pkgname": "dmenu",
      "arch": "dmenu",
      "void": "dmenu"
    },
    {
      "pkgname": "lynx",
      "arch": "lynx",
      "void": "lynx"
    },
    {
      "pkgname": "fzf",
      "arch": "fzf",
      "void": "fzf"
    },
    {
      "pkgname": "bat",
      "arch": "bat",
      "void": "bat"
    },
    {
      "pkgname": "ffmpeg",
      "arch": "ffmpeg",
      "void": "ffmpeg"
    },
    {
      "pkgname": "youtube-dl",
      "arch": "youtube-dl",
      "void": "youtube-dl"
    },
    {
      "pkgname": "",
      "arch": "",
      "void": ""
    }
  ]
}
"""
def __generate_database_file(path):
    with open(path) as f:
        f.writelines(templ)
    f.close()
