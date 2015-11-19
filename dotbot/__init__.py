from typing import Any, Sequence
import random


class Ticket(object):

    def __init__(
        self,
        owner=None,
        repo=None,
        issue_number=None,
        assignee=None
    ):
        if None in [owner, repo, issue_number]:
            raise TicketError("Insufficent details to update the ticket")
        self.owner = owner
        self.repo = repo
        self.issue_number = issue_number
        self.assignee = assignee


class TicketDelta(object):

    def __init__(
        self,
        owner=None,
        repo=None,
        issue_number=None,
        comment=None,
        assignee=None
    ):
        if None in [owner, repo, issue_number]:
            raise TicketError("Insufficent details to update the ticket")
        self.owner = owner
        self.repo = repo
        self.issue_number = issue_number
        self.comment = comment
        self.assignee = assignee

    def __eq__(self, other: Any):
        if isinstance(other, TicketDelta):
            return str(self) == str(other)
        return False

    def __str__(self):
        s = "TicketDelta<"
        s += "owner=" + str(self.owner)
        s += ",repo=" + str(self.repo)
        s += ",issue_number=" + str(self.issue_number)
        s += ",comment=" + str(self.comment)
        s += ",assignee=" + str(self.assignee)
        s += ">"
        return s

    def __repr__(self):
        return self.__str__()


class TeamMember(object):

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other: Any):
        if isinstance(other, TeamMember):
            return str(self) == str(other)
        return False

    def __str__(self):
        return "TeamMember<name=" + str(self.name) + ">"

    def __repr__(self):
        return self.__str__()


def assign(ticket: Ticket, team: Sequence[TeamMember]) -> TicketDelta:
    if len(team) < 2:
        return TicketDelta(
            ticket.owner,
            ticket.repo,
            ticket.issue_number,
            comment="Cannot assign a DoT with a team of " + str(len(team)) + " people."
        )

    asignee = random.choice([tm.name for tm in team if tm.name != ticket.assignee])

    return TicketDelta(
        owner=ticket.owner,
        repo=ticket.repo,
        issue_number=ticket.issue_number,
        assignee=asignee
    )
