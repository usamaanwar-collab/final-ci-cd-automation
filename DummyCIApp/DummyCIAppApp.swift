//
//  DummyCIAppApp.swift
//  DummyCIApp
//
//  Created by EvolveDash on 17/04/2026.
//

import SwiftUI
import CoreData

@main
struct DummyCIAppApp: App {
    let persistenceController = PersistenceController.shared

    var body: some Scene {
        WindowGroup {
            ContentView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
