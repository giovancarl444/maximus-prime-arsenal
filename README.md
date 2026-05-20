# Maximus Prime Arsenal

Unified launcher and toolchain for the Maximus Prime AIOS stack.

## Components

- **OpenBB API** (port 6900) — Financial data server
- **Killshot Dashboard** (port 7777) — Live trading dashboard
- **OpenBB Daemon** — Background data fetcher
- **Scanner Loop** — Continuous 15m scanner
- **Monitor Services** — Service health monitor

## Usage

```bash
# Launch all components
python3 launcher.py

# Or use the Hermes skill
hermes run maximus-prime-arsenal
```

## Status

All components launch in order with port verification. Required components that fail will abort the launch.

## Requirements

- Python 3.9+
- killshot repo at `/Users/midas/Code/killshot`
- openbb-env at `/Users/midas/Code/openbb-env`
- Maximus Prime stack operational

## Author

Vachia (Svee) — architect of Maximus Prime.
