import Foundation

public extension Bundle {
    static func load(demo: Bool) -> String? {
        guard let path = Bundle.main.path(forResource: demo ? "input-demo" : "input", ofType: "txt") else { return nil }
        let url = URL(fileURLWithPath: path)
        guard let data = try? Data(contentsOf: url) else { return nil }
        return String(data: data, encoding: .utf8)
    }
}
