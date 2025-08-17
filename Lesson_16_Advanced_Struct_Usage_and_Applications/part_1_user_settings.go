type UserSettings struct {
    theme         string
    notifications bool
    language      string
}

func NewUserSettings() UserSettings {
    return UserSettings{
        theme:         "light",       // default value
        notifications: true,          // default value
        language:      "English",     // default value
    }
}
