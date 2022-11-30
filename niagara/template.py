def generate_database_file(path):
    templ = """
{
  "packages": [
    {
      "pkgname": "picom",
      "arch": "picom",
      "void": "picom",
      "fedora": "picom",
      "debian": "picom",
      "gentoo": "x11-misc/picom"
    },
    {
      "pkgname": "kitty",
      "arch": "kitty",
      "void": "kitty",
      "fedora": "kitty",
      "debian": "kitty",
      "gentoo": "x11-terms/kitty"
    },
    {
      "pkgname": "alacritty",
      "arch": "alacritty",
      "void": "alacritty",
      "fedora": "alacritty",
      "debian": "",
      "gentoo": "x11-terms/alacritty"
    },
    {
      "pkgname": "neofetch",
      "arch": "neofetch",
      "void": "neofetch",
      "fedora": "neofetch",
      "debian": "neofetch",
      "gentoo": "app-misc/neofetch"
    },
    {
      "pkgname": "feh",
      "arch": "feh",
      "void": "feh",
      "fedora": "feh",
      "debian": "feh",
      "gentoo": "media-gfx/feh"
    },
    {
      "pkgname": "emacs",
      "arch": "emacs",
      "void": "emacs",
      "fedora": "emacs",
      "debian": "emacs",
      "gentoo": "app-editors/emacs"
    },
    {
      "pkgname": "vim",
      "arch": "vim",
      "void": "vim",
      "fedora": "vim",
      "debian": "vim",
      "gentoo": "app-editors/vim"
    },
    {
      "pkgname": "neovim",
      "arch": "neovim",
      "void": "neovim",
      "fedora": "neovim",
      "debian": "neovim",
      "gentoo": "app-editors/neovim"
    },
    {
      "pkgname": "rofi",
      "arch": "rofi",
      "void": "rofi",
      "fedora": "rofi",
      "debian": "rofi",
      "gentoo": "x11-misc/rofi"
    },
    {
      "pkgname": "flameshot",
      "arch": "flameshot",
      "void": "flameshot",
      "fedora": "flameshot",
      "debian": "flameshot",
      "gentoo": "media-gfx/flameshot"
    },
    {
      "pkgname": "doas",
      "arch": "opendoas",
      "void": "opendoas",
      "fedora": "opendoas",
      "debian": "doas", # > Debian 11
      "gentoo": "app-admin/doas"
    },
    {
      "pkgname": "dunst",
      "arch": "dunst",
      "void": "dunst",
      "fedora": "dunst",
      "debian": "dunst",
      "gentoo": "x11-misc/dunst"
    },
    {
      "pkgname": "firefox",
      "arch": "firefox",
      "void": "firefox",
      "fedora": "firefox",
      "debian": "firefox",
      "gentoo": "www-client/firefox-bin"
    },
    {
      "pkgname": "ripgrep",
      "arch": "ripgrep",
      "void": "ripgrep",
      "fedora": "ripgrep",
      "debian": "ripgrep",
      "gentoo": "sys-apps/ripgrep"
    },
    {
      "pkgname": "mpv",
      "arch": "mpv",
      "void": "mpv",
      "fedora": "mpv",
      "debian": "mpv",
      "gentoo": "media-video/mpv"
    },
    {
      "pkgname": "dmenu",
      "arch": "dmenu",
      "void": "dmenu",
      "fedora": "dmenu",
      "debian": "dmenu",
      "gentoo": "x11-misc/dmenu"
    },
    {
      "pkgname": "lynx",
      "arch": "lynx",
      "void": "lynx",
      "fedora": "lynx",
      "debian": "lynx",
      "gentoo": "www-client/lynx"
    },
    {
      "pkgname": "fzf",
      "arch": "fzf",
      "void": "fzf",
      "fedora": "fzf",
      "debian": "fzf",
      "gentoo": "app-shells/fzf"
    },
    {
      "pkgname": "bat",
      "arch": "bat",
      "void": "bat",
      "fedora": "bat",
      "debian": "bat",
      "gentoo": "sys-apps/bat"
    },
    {
      "pkgname": "ffmpeg",
      "arch": "ffmpeg",
      "void": "ffmpeg",
      "fedora": "ffmpeg",
      "debian": "ffmpeg",
      "gentoo": "media-video/ffmpeg"
    },
    {
      "pkgname": "ytdl",
      "arch": "youtube-dl",
      "void": "youtube-dl",
      "fedora": "youtube-dl",
      "debian": "youtube-dl",
      "gentoo": "net-misc/youtube-dl"
    },
    {
      "pkgname": "sway",
      "arch": "sway",
      "void": "",
      "fedora": "sway",
      "debian": "sway", # > Debian 11
      "gentoo": "gui-wm/sway"
    },
    {
      "pkgname": "xorg",
      "arch": "xorg",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "xinit",
      "arch": "xorg-xinit",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      # i3 and i3-gaps are getting merged sometime in the future, look out for that in the repos of each distro
      "pkgname": "i3",
      "arch": "i3-gaps",
      "void": "",
      "fedora": "i3-gaps",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "bspwm",
      "arch": "bspwm",
      "void": "",
      "fedora": "bspwm",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "xinerama",
      "arch": "libxinerama",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "waybar",
      "arch": "waybar",
      "void": "",
      "fedora": "waybar",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "swaybg",
      "arch": "swaybg",
      "void": "",
      "fedora": "swaybg",
      "debian": "",
      "gentoo": "" # Not applicable
    },
    {
      "pkgname": "mpd",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "wofi",
      "arch": "",
      "void": "",
      "fedora": "wofi",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    },
    {
      "pkgname": "",
      "arch": "",
      "void": "",
      "fedora": "",
      "debian": "",
      "gentoo": ""
    }

  ]
}
"""
    with open(path, 'w+') as f:
        f.writelines(templ)
    f.close()


