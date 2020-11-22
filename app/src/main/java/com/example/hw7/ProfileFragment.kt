package com.example.hw7

import android.os.Bundle
import androidx.preference.PreferenceFragmentCompat

class ProfileFragment : PreferenceFragmentCompat() {

    override fun onCreatePreferences(savedInstanceState: Bundle?, rootKey: String?) {
        setPreferencesFromResource(R.xml.root_preferences, rootKey)
    }
}