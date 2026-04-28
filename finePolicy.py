class FinePolicy:
    def computeFine(self, daysOverdue):
        if daysOverdue <= 0: return 0
        if daysOverdue > 16: return min(10 * daysOverdue, 500)
        if daysOverdue >= 8: return 5 * daysOverdue
        return 2 * daysOverdue
