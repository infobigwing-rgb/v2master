# Release Signing Configuration

This document explains how to safely manage your Android signing keystore and release credentials.

## Keystore Setup

- The signing scripts generate a new keystore at `android_admin_apk/release.keystore` if one does not already exist.
- The alias is `unlock_tool_release` by default.
- The example scripts use the placeholder password `changeit`; replace this with a strong password before publishing.

## Backup Recommendations

- Back up the keystore file to at least two secure locations.
- Record both the store password and the key password in a password manager.
- Losing the keystore or passwords will make it impossible to update the signed APK.

## Production Signing Workflow

1. Generate or reuse an existing keystore.
2. Build a release APK with Gradle.
3. Sign the APK with `apksigner`.
4. Align the signed APK with `zipalign`.
5. Keep the keystore and password secret.

## Important Notes

- Do not commit the keystore to version control.
- If you use an existing keystore, update the `ALIAS` and password settings in `scripts/sign_apk.sh` and `scripts/sign_apk.bat`.
- Use a high-entropy password and a secure passphrase.
