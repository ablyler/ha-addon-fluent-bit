# ha-addon-fluent-bit
Home Assistant Addon for Fluent Bit

![Supports aarch64 Architecture][aarch64-shield]
![Supports amd64 Architecture][amd64-shield]

## Configuration
Place the configuration file in the `/addon_configs/*_fluent_bit` directory on the Home Assistant server. By default the addon will look for a file named `fluent_bit.conf` in this directory.

I recommend using the `File Editor` addon to create and edit the configuration file. You can find the `File Editor` addon in the Home Assistant Community Add-ons repository. After installing the addon you will need to turn off the `Enforce Basepath` option in the addon configuration. This will allow you to access the `/addon_configs` directory.

Please note that this directory will not be created until you start the addon for the first time. The start of the path will also contain some random characters, so the full path will look something like `/addon_configs/abc123_fluent_bit`.

### Example Configuration
Below is an example configuration file for Fluent Bit. This configuration will read logs from the systemd journal. You would need to add an output section to send the logs to your desired destination. For a list of supported outputs see the [Fluent Bit documentation](https://docs.fluentbit.io/manual/pipeline/outputs).

```conf
[INPUT]
  Name systemd
  Path /var/log/journal
  DB /data/fluent-bit.db
```

## Installation

[![Open your Home Assistant instance and show the add add-on repository dialog with a specific repository URL pre-filled.](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Fablyler%2Fha-addon-fluent-bit)

Use the button above to add this repository to your Home Assistant instance. Once added, you can install the `Fluent Bit` add-on.

[aarch64-shield]: https://img.shields.io/badge/aarch64-yes-green.svg
[amd64-shield]: https://img.shields.io/badge/amd64-yes-green.svg
