from dotbot import assign, TicketDelta, Ticket, TeamMember


def eq(left, right):
    assert left == right


def test_assign_with_less_than_two_team_members():
    eq(
        TicketDelta(
            owner="smallco",
            repo="bigproj",
            issue_number=1,
            comment="Cannot assign a DoT with a team of 0 people."
        ),
        assign(
            Ticket(
                owner="smallco",
                repo="bigproj",
                issue_number=1
            ),
            []
        )
    )


def test_assign_with_two_team_members():
    eq(
        TicketDelta(
            owner="smallco",
            repo="bigproj",
            issue_number=1,
            assignee="Bob",
            comment="DoTBot reassigned to Bob for review and testing."
        ),
        assign(
            Ticket(
                owner="smallco",
                repo="bigproj",
                issue_number=1,
                assignee="Alicia"
            ),
            [
                TeamMember("Alicia"),
                TeamMember("Bob")
            ]
        )
    )
