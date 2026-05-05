import XCTest // <--- This line is missing!

final class DummyCIAppTests: XCTestCase {

    func testExample() throws {
        let x = 2 + 2
        XCTAssertEqual(x, 4, "Math should still work!")
    }
}
